# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseUsageImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseUsageImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/VerificationCaseUsageImpl.java
- source_bytes: 5809
- source_sha256: `22f5d9be58a5f63e8a265124af47b49f77a1bf6dc59485859baf8b8a2406040f`
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
import org.omg.sysml.lang.sysml.VerificationCaseUsage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Verification Case Usage</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.VerificationCaseUsageImpl#getVerificationCaseDefinition <em>Verification Case Definition</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.VerificationCaseUsageImpl#getVerifiedRequirement <em>Verified Requirement</em>}</li>
 * </ul>
 *
 * @generated
 */
public class VerificationCaseUsageImpl extends CaseUsageImpl implements VerificationCaseUsage {
	/**
	 * The cached setting delegate for the '{@link #getVerificationCaseDefinition() <em>Verification Case Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getVerificationCaseDefinition()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate VERIFICATION_CASE_DEFINITION__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.VERIFICATION_CASE_USAGE__VERIFICATION_CASE_DEFINITION).getSettingDelegate();

	/**
	 * The cached setting delegate for the '{@link #getVerifiedRequirement() <em>Verified Requirement</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getVerifiedRequirement()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate VERIFIED_REQUIREMENT__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.VERIFICATION_CASE_USAGE__VERIFIED_REQUIREMENT).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected VerificationCaseUsageImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.VERIFICATION_CASE_USAGE;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public VerificationCaseDefinition getVerificationCaseDefinition() {
		return (VerificationCaseDefinition)VERIFICATION_CASE_DEFINITION__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public VerificationCaseDefinition basicGetVerificationCaseDefinition() {
		return (VerificationCaseDefinition)VERIFICATION_CASE_DEFINITION__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setVerificationCaseDefinition(VerificationCaseDefinition newVerificationCaseDefinition) {
		VERIFICATION_CASE_DEFINITION__ESETTING_DELEGATE.dynamicSet(this, null, 0, newVerificationCaseDefinition);
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
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFICATION_CASE_DEFINITION:
				if (resolve) return getVerificationCaseDefinition();
				return basicGetVerificationCaseDefinition();
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFIED_REQUIREMENT:
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
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFICATION_CASE_DEFINITION:
				setVerificationCaseDefinition((VerificationCaseDefinition)newValue);
				return;
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFIED_REQUIREMENT:
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
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFICATION_CASE_DEFINITION:
				setVerificationCaseDefinition((VerificationCaseDefinition)null);
				return;
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFIED_REQUIREMENT:
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
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFICATION_CASE_DEFINITION:
				return VERIFICATION_CASE_DEFINITION__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
			case SysMLPackage.VERIFICATION_CASE_USAGE__VERIFIED_REQUIREMENT:
				return VERIFIED_REQUIREMENT__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
		}
		return super.eIsSet(featureID);
	}

} //VerificationCaseUsageImpl

````
