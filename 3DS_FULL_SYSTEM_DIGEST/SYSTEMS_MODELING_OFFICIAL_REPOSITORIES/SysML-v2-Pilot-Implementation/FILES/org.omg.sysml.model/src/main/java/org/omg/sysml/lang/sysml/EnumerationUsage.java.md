# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationUsage.java
- source_bytes: 2321
- source_sha256: `cda672e9ae87fa30c4ec8044d13793deedab8a371842916c9545c13bc1d04e61`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Enumeration Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>EnumerationUsage</code> is an <code>AttributeUsage</code> whose <code>attributeDefinition</code> is an <code>EnumerationDefinition</code>.</p>
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.EnumerationUsage#getEnumerationDefinition <em>Enumeration Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getEnumerationUsage()
 * @model
 * @generated
 */
public interface EnumerationUsage extends AttributeUsage {
	/**
	 * Returns the value of the '<em><b>Enumeration Definition</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.AttributeUsage#getAttributeDefinition() <em>Attribute Definition</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The single EnumerationDefinition that is the type of this EnumerationUsage.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Enumeration Definition</em>' reference.
	 * @see #setEnumerationDefinition(EnumerationDefinition)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getEnumerationUsage_EnumerationDefinition()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='definedEnumeration'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EnumerationDefinition getEnumerationDefinition();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.EnumerationUsage#getEnumerationDefinition <em>Enumeration Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Enumeration Definition</em>' reference.
	 * @see #getEnumerationDefinition()
	 * @generated
	 */
	void setEnumerationDefinition(EnumerationDefinition value);

} // EnumerationUsage

````
