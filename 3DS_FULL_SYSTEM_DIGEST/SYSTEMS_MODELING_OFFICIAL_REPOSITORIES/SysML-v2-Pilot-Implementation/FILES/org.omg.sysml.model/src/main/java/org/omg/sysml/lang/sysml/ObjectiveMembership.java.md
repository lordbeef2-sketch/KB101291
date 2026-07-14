# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ObjectiveMembership.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ObjectiveMembership.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ObjectiveMembership.java
- source_bytes: 2679
- source_sha256: `ae72655dead480bf1bbaf9206d711ae4afe1c2c1e699c8c974e07929c4febf19`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Objective Membership</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>ObjectiveMembership</code> is a <code>FeatureMembership</code> that indicates that its <code>ownedObjectiveRequirement</code> is the objective <code>RequirementUsage</code> for its <code>owningType</code>, which must be a <code>CaseDefinition</code> or <code>CaseUsage</code>.</p>
 * owningType.oclIsType(CaseDefinition) or
 * owningType.oclIsType(CaseUsage)
 * 
 * ownedObjectiveRequirement.isComposite
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.ObjectiveMembership#getOwnedObjectiveRequirement <em>Owned Objective Requirement</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getObjectiveMembership()
 * @model
 * @generated
 */
public interface ObjectiveMembership extends FeatureMembership {
	/**
	 * Returns the value of the '<em><b>Owned Objective Requirement</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.FeatureMembership#getOwnedMemberFeature() <em>Owned Member Feature</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The RequirementUsage that is the <code>ownedMemberFeature</code> of this RequirementUsage.</p> 
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Owned Objective Requirement</em>' reference.
	 * @see #setOwnedObjectiveRequirement(RequirementUsage)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getObjectiveMembership_OwnedObjectiveRequirement()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='owningObjectiveMembership'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	RequirementUsage getOwnedObjectiveRequirement();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.ObjectiveMembership#getOwnedObjectiveRequirement <em>Owned Objective Requirement</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Owned Objective Requirement</em>' reference.
	 * @see #getOwnedObjectiveRequirement()
	 * @generated
	 */
	void setOwnedObjectiveRequirement(RequirementUsage value);

} // ObjectiveMembership

````
