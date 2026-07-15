# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/CaseDefinitionImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/CaseDefinitionImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/CaseDefinitionImpl.java
- source_bytes: 7154
- source_sha256: `2ed4c2bba243e8e003182e9ba9f70789988d58906b67cd4adee1084835cd67fa`
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

import org.omg.sysml.lang.sysml.CaseDefinition;
import org.omg.sysml.lang.sysml.PartUsage;
import org.omg.sysml.lang.sysml.RequirementUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.Usage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Case Definition</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.CaseDefinitionImpl#getActorParameter <em>Actor Parameter</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.CaseDefinitionImpl#getObjectiveRequirement <em>Objective Requirement</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.CaseDefinitionImpl#getSubjectParameter <em>Subject Parameter</em>}</li>
 * </ul>
 *
 * @generated
 */
public class CaseDefinitionImpl extends CalculationDefinitionImpl implements CaseDefinition {
	/**
	 * The cached setting delegate for the '{@link #getActorParameter() <em>Actor Parameter</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getActorParameter()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate ACTOR_PARAMETER__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.CASE_DEFINITION__ACTOR_PARAMETER).getSettingDelegate();

	/**
	 * The cached setting delegate for the '{@link #getObjectiveRequirement() <em>Objective Requirement</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getObjectiveRequirement()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate OBJECTIVE_REQUIREMENT__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.CASE_DEFINITION__OBJECTIVE_REQUIREMENT).getSettingDelegate();

	/**
	 * The cached setting delegate for the '{@link #getSubjectParameter() <em>Subject Parameter</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getSubjectParameter()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate SUBJECT_PARAMETER__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.CASE_DEFINITION__SUBJECT_PARAMETER).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected CaseDefinitionImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.CASE_DEFINITION;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public RequirementUsage getObjectiveRequirement() {
		return (RequirementUsage)OBJECTIVE_REQUIREMENT__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public RequirementUsage basicGetObjectiveRequirement() {
		return (RequirementUsage)OBJECTIVE_REQUIREMENT__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setObjectiveRequirement(RequirementUsage newObjectiveRequirement) {
		OBJECTIVE_REQUIREMENT__ESETTING_DELEGATE.dynamicSet(this, null, 0, newObjectiveRequirement);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Usage getSubjectParameter() {
		return (Usage)SUBJECT_PARAMETER__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Usage basicGetSubjectParameter() {
		return (Usage)SUBJECT_PARAMETER__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setSubjectParameter(Usage newSubjectParameter) {
		SUBJECT_PARAMETER__ESETTING_DELEGATE.dynamicSet(this, null, 0, newSubjectParameter);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public EList<PartUsage> getActorParameter() {
		return (EList<PartUsage>)ACTOR_PARAMETER__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.CASE_DEFINITION__ACTOR_PARAMETER:
				return getActorParameter();
			case SysMLPackage.CASE_DEFINITION__OBJECTIVE_REQUIREMENT:
				if (resolve) return getObjectiveRequirement();
				return basicGetObjectiveRequirement();
			case SysMLPackage.CASE_DEFINITION__SUBJECT_PARAMETER:
				if (resolve) return getSubjectParameter();
				return basicGetSubjectParameter();
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
			case SysMLPackage.CASE_DEFINITION__ACTOR_PARAMETER:
				getActorParameter().clear();
				getActorParameter().addAll((Collection<? extends PartUsage>)newValue);
				return;
			case SysMLPackage.CASE_DEFINITION__OBJECTIVE_REQUIREMENT:
				setObjectiveRequirement((RequirementUsage)newValue);
				return;
			case SysMLPackage.CASE_DEFINITION__SUBJECT_PARAMETER:
				setSubjectParameter((Usage)newValue);
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
			case SysMLPackage.CASE_DEFINITION__ACTOR_PARAMETER:
				getActorParameter().clear();
				return;
			case SysMLPackage.CASE_DEFINITION__OBJECTIVE_REQUIREMENT:
				setObjectiveRequirement((RequirementUsage)null);
				return;
			case SysMLPackage.CASE_DEFINITION__SUBJECT_PARAMETER:
				setSubjectParameter((Usage)null);
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
			case SysMLPackage.CASE_DEFINITION__ACTOR_PARAMETER:
				return ACTOR_PARAMETER__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
			case SysMLPackage.CASE_DEFINITION__OBJECTIVE_REQUIREMENT:
				return OBJECTIVE_REQUIREMENT__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
			case SysMLPackage.CASE_DEFINITION__SUBJECT_PARAMETER:
				return SUBJECT_PARAMETER__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
		}
		return super.eIsSet(featureID);
	}

} //CaseDefinitionImpl

````
