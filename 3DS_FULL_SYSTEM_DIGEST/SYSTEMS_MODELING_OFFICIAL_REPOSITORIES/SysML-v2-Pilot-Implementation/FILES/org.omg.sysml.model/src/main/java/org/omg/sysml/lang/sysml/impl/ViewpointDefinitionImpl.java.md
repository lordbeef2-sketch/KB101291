# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ViewpointDefinitionImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ViewpointDefinitionImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ViewpointDefinitionImpl.java
- source_bytes: 3479
- source_sha256: `327608034afa31b9d9334a5d5981029d3c4b700896a3db1a623d35f09c38cadc`
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

import org.omg.sysml.lang.sysml.PartUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.ViewpointDefinition;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Viewpoint Definition</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.ViewpointDefinitionImpl#getViewpointStakeholder <em>Viewpoint Stakeholder</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ViewpointDefinitionImpl extends RequirementDefinitionImpl implements ViewpointDefinition {
	/**
	 * The cached setting delegate for the '{@link #getViewpointStakeholder() <em>Viewpoint Stakeholder</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getViewpointStakeholder()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate VIEWPOINT_STAKEHOLDER__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.VIEWPOINT_DEFINITION__VIEWPOINT_STAKEHOLDER).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ViewpointDefinitionImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.VIEWPOINT_DEFINITION;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public EList<PartUsage> getViewpointStakeholder() {
		return (EList<PartUsage>)VIEWPOINT_STAKEHOLDER__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.VIEWPOINT_DEFINITION__VIEWPOINT_STAKEHOLDER:
				return getViewpointStakeholder();
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
			case SysMLPackage.VIEWPOINT_DEFINITION__VIEWPOINT_STAKEHOLDER:
				getViewpointStakeholder().clear();
				getViewpointStakeholder().addAll((Collection<? extends PartUsage>)newValue);
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
			case SysMLPackage.VIEWPOINT_DEFINITION__VIEWPOINT_STAKEHOLDER:
				getViewpointStakeholder().clear();
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
			case SysMLPackage.VIEWPOINT_DEFINITION__VIEWPOINT_STAKEHOLDER:
				return VIEWPOINT_STAKEHOLDER__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
		}
		return super.eIsSet(featureID);
	}

} //ViewpointDefinitionImpl

````
