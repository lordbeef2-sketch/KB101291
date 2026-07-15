# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Invariant.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Invariant.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Invariant.java
- source_bytes: 1995
- source_sha256: `96880d006112ed521ab68980b87934a749a221b72879029da69e1251669ba0eb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Invariant</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>Invariant</code> is a <code>BooleanExpression</code> that is asserted to have a specific <code><em>Boolean</em></code> result value. If <code>isNegated = false</code>, then the result is asserted to be true. If <code>isNegated = true</code>, then the result is asserted to be false.</p>
 * 
 * if isNegated then
 *     specializesFromLibrary('Performances::falseEvaluations')
 * else
 *     specializesFromLibrary('Performances::trueEvaluations')
 * endif
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Invariant#isNegated <em>Is Negated</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInvariant()
 * @model
 * @generated
 */
public interface Invariant extends BooleanExpression {
	/**
	 * Returns the value of the '<em><b>Is Negated</b></em>' attribute.
	 * The default value is <code>"false"</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Whether this <code>Invariant</code> is asserted to be false rather than true.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Is Negated</em>' attribute.
	 * @see #setIsNegated(boolean)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getInvariant_IsNegated()
	 * @model default="false" required="true" ordered="false"
	 * @generated
	 */
	boolean isNegated();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.Invariant#isNegated <em>Is Negated</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Is Negated</em>' attribute.
	 * @see #isNegated()
	 * @generated
	 */
	void setIsNegated(boolean value);

} // Invariant

````
