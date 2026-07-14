# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/StakeholderMembership.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/StakeholderMembership.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/StakeholderMembership.java
- source_bytes: 2649
- source_sha256: `e1a6979c7382e95a46f6894ff095d3cc5d1d8083dc7c51763b08e4b4135d323e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Stakeholder Membership</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>StakeholderMembership</code> is a <code>ParameterMembership</code> that identifies a <code>PartUsage</code> as a <code>stakeholderParameter</code> of a <code>RequirementDefinition</code> or <code>RequirementUsage</code>, which specifies a role played by an entity with concerns framed by the <code>owningType</code>.</p>
 * owningType.oclIsKindOf(RequirementUsage) or
 * owningType.oclIsKindOf(RequirementDefinition)
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.StakeholderMembership#getOwnedStakeholderParameter <em>Owned Stakeholder Parameter</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getStakeholderMembership()
 * @model
 * @generated
 */
public interface StakeholderMembership extends ParameterMembership {
	/**
	 * Returns the value of the '<em><b>Owned Stakeholder Parameter</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.ParameterMembership#getOwnedMemberParameter() <em>Owned Member Parameter</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>PartUsage</code> specifying the stakeholder.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Owned Stakeholder Parameter</em>' reference.
	 * @see #setOwnedStakeholderParameter(PartUsage)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getStakeholderMembership_OwnedStakeholderParameter()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='owningStakeholderMembership'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	PartUsage getOwnedStakeholderParameter();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.StakeholderMembership#getOwnedStakeholderParameter <em>Owned Stakeholder Parameter</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Owned Stakeholder Parameter</em>' reference.
	 * @see #getOwnedStakeholderParameter()
	 * @generated
	 */
	void setOwnedStakeholderParameter(PartUsage value);

} // StakeholderMembership

````
