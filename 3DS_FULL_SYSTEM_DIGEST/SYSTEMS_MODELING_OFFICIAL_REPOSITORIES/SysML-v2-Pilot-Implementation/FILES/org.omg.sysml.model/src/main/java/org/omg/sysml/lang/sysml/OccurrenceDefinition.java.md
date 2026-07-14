# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/OccurrenceDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/OccurrenceDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/OccurrenceDefinition.java
- source_bytes: 2310
- source_sha256: `da82fbc433a8f28923e996d54cafe52a5c7797268a552c3ee3d5928666d14a55`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Occurrence Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>OccurrenceDefinition</code> is a <code>Definition</code> of a <code>Class</code> of individuals that have an independent life over time and potentially an extent over space. This includes both structural things and behaviors that act on such structures. If <code>isIndividual</code> is true, then the <code>OccurrenceDefinition</code> is constrained to have (at most) a single instance that is the entire life of a single individual.</p>
 * isIndividual implies specializesFromLibrary('Occurrences::Life')
 * isIndividual implies
 *     multiplicity <> null and
 *     multiplicity.specializesFromLibrary('Base::zeroOrOne')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.OccurrenceDefinition#isIndividual <em>Is Individual</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getOccurrenceDefinition()
 * @model
 * @generated
 */
public interface OccurrenceDefinition extends Definition, org.omg.sysml.lang.sysml.Class {
	/**
	 * Returns the value of the '<em><b>Is Individual</b></em>' attribute.
	 * The default value is <code>"false"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Whether this <code>OccurrenceDefinition</code> is constrained to represent at most one thing.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Is Individual</em>' attribute.
	 * @see #setIsIndividual(boolean)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getOccurrenceDefinition_IsIndividual()
	 * @model default="false" required="true" ordered="false"
	 * @generated
	 */
	boolean isIndividual();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.OccurrenceDefinition#isIndividual <em>Is Individual</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Is Individual</em>' attribute.
	 * @see #isIndividual()
	 * @generated
	 */
	void setIsIndividual(boolean value);

} // OccurrenceDefinition

````
