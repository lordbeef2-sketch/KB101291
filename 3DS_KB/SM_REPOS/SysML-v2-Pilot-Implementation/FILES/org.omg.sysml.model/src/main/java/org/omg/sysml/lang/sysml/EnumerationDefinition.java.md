# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/EnumerationDefinition.java
- source_bytes: 2297
- source_sha256: `dcfd961118323a2a482a25e01bdd0fadcca359fce59ba3856587306a162731ba`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Enumeration Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>EnumerationDefinition</code> is an <code>AttributeDefinition</code> all of whose instances are given by an explicit list of <code>enumeratedValues</code>. This is realized by requiring that the <code>EnumerationDefinition</code> have <code>isVariation = true</code>, with the <code>enumeratedValues</code> being its <code>variants</code>.</p> 
 * isVariation
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.EnumerationDefinition#getEnumeratedValue <em>Enumerated Value</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getEnumerationDefinition()
 * @model
 * @generated
 */
public interface EnumerationDefinition extends AttributeDefinition {
	/**
	 * Returns the value of the '<em><b>Enumerated Value</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.EnumerationUsage}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Definition#getVariant() <em>Variant</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p><code>EnumerationUsages</code> of this <code>EnumerationDefinition</code>that have distinct, fixed values. Each <code>enumeratedValue</code> specifies one of the allowed instances of the <code>EnumerationDefinition</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Enumerated Value</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getEnumerationDefinition_EnumeratedValue()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='owningEnumerationDefinition'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<EnumerationUsage> getEnumeratedValue();

} // EnumerationDefinition

````
