# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ElementFilterMembership.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ElementFilterMembership.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ElementFilterMembership.java
- source_bytes: 2811
- source_sha256: `a8f5367c7ee2afde1bc1c58b8ca40eb6833a4b3f8951449914617bf44092ca9c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Element Filter Membership</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p><code>ElementFilterMembership</code> is a <code>Membership</code> between a <code>Namespace</code> and a model-level evaluable <code><em>Boolean</em></code>-valued <code>Expression</code>, asserting that imported <code>members</code> of the <code>Namespace</code> should be filtered using the <code>condition</code> <code>Expression</code>. A general <code>Namespace</code> does not define any specific filtering behavior, but such behavior may be defined for various specialized kinds of <code>Namespaces</code>.</p>
 * 
 * condition.isModelLevelEvaluable
 * condition.result.specializesFromLibrary('ScalarValues::Boolean')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.ElementFilterMembership#getCondition <em>Condition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getElementFilterMembership()
 * @model
 * @generated
 */
public interface ElementFilterMembership extends OwningMembership {
	/**
	 * Returns the value of the '<em><b>Condition</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.OwningMembership#getOwnedMemberElement() <em>Owned Member Element</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The model-level evaluable <code>Boolean</code>-valued <code>Expression</code> used to filter the imported <code>members</code> of the <code>membershipOwningNamespace</code> of this <code>ElementFilterMembership</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Condition</em>' reference.
	 * @see #setCondition(Expression)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getElementFilterMembership_Condition()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='owningFilter'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Expression getCondition();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.ElementFilterMembership#getCondition <em>Condition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Condition</em>' reference.
	 * @see #getCondition()
	 * @generated
	 */
	void setCondition(Expression value);

} // ElementFilterMembership

````
