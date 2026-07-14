# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseDefinitionImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseDefinitionImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseDefinitionImpl.java
- source_bytes: 3580
- source_sha256: `5dad012821aad3d1fbae25e17ca8358f4257ba4175143e7fb7ff97859397b85c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml.impl;

import java.util.Collection;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;

import org.omg.sysml.lang.sysml.RequirementUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.VerificationCaseDefinition;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Verification Case Definition</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.VerificationCaseDefinitionImpl#getVerifiedRequirement <em>Verified Requirement</em>}</li>
 * </ul>
 *
 * @generated
 */
public class VerificationCaseDefinitionImpl extends CaseDefinitionImpl implements VerificationCaseDefinition {
	/**
	 * The cached setting delegate for the '{@link #getVerifiedRequirement() <em>Verified Requirement</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getVerifiedRequirement()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate VERIFIED_REQUIREMENT__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.VERIFICATION_CASE_DEFINITION__VERIFIED_REQUIREMENT).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected VerificationCaseDefinitionImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.VERIFICATION_CASE_DEFINITION;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public EList<RequirementUsage> getVerifiedRequirement() {
		return (EList<RequirementUsage>)VERIFIED_REQUIREMENT__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.VERIFICATION_CASE_DEFINITION__VERIFIED_REQUIREMENT:
				return getVerifiedRequirement();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case SysMLPackage.VERIFICATION_CASE_DEFINITION__VERIFIED_REQUIREMENT:
				getVerifiedRequirement().clear();
				getVerifiedRequirement().addAll((Collection<? extends RequirementUsage>)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case SysMLPackage.VERIFICATION_CASE_DEFINITION__VERIFIED_REQUIREMENT:
				getVerifiedRequirement().clear();
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case SysMLPackage.VERIFICATION_CASE_DEFINITION__VERIFIED_REQUIREMENT:
				return VERIFIED_REQUIREMENT__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
		}
		return super.eIsSet(featureID);
	}

} //VerificationCaseDefinitionImpl

````
