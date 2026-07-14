# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/VerificationCaseDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/VerificationCaseDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/VerificationCaseDefinition.java
- source_bytes: 2281
- source_sha256: `cc566ad12adb2538f6c6182b2fe4aee7ea59e32fd612d8ba5f803c542f064148`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Verification Case Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>VerificationCaseDefinition</code> is a <code>CaseDefinition</code> for the purpose of verification of the subject of the case against its requirements.</p>
 * verifiedRequirement =
 *     if objectiveRequirement = null then OrderedSet{}
 *     else 
 *         objectiveRequirement.featureMembership->
 *             selectByKind(RequirementVerificationMembership).
 *             verifiedRequirement->asOrderedSet()
 *     endif
 * specializesFromLibrary('VerificationCases::VerificationCase')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.VerificationCaseDefinition#getVerifiedRequirement <em>Verified Requirement</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getVerificationCaseDefinition()
 * @model
 * @generated
 */
public interface VerificationCaseDefinition extends CaseDefinition {
	/**
	 * Returns the value of the '<em><b>Verified Requirement</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.RequirementUsage}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>RequirementUsages</code> verified by this <code>VerificationCaseDefinition</code>, which are the <code>verifiedRequirements</code> of all <code>RequirementVerificationMemberships</code> of the <code>objectiveRequirement</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Verified Requirement</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getVerificationCaseDefinition_VerifiedRequirement()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='verifyingCaseDefinition'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<RequirementUsage> getVerifiedRequirement();

} // VerificationCaseDefinition

````
