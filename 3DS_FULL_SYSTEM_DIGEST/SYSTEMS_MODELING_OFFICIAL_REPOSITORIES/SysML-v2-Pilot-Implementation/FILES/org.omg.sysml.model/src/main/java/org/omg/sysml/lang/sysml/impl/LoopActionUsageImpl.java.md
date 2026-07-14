# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/LoopActionUsageImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/LoopActionUsageImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/LoopActionUsageImpl.java
- source_bytes: 3558
- source_sha256: `5624e3c95f0856b0974ffd81c83e68e3ed09eab78f79dc521d749310f8fa594d`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml.impl;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;

import org.omg.sysml.lang.sysml.ActionUsage;
import org.omg.sysml.lang.sysml.LoopActionUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Loop Action Usage</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.LoopActionUsageImpl#getBodyAction <em>Body Action</em>}</li>
 * </ul>
 *
 * @generated
 */
public abstract class LoopActionUsageImpl extends ActionUsageImpl implements LoopActionUsage {
	/**
	 * The cached setting delegate for the '{@link #getBodyAction() <em>Body Action</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getBodyAction()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate BODY_ACTION__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.LOOP_ACTION_USAGE__BODY_ACTION).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected LoopActionUsageImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.LOOP_ACTION_USAGE;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public ActionUsage getBodyAction() {
		return (ActionUsage)BODY_ACTION__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public ActionUsage basicGetBodyAction() {
		return (ActionUsage)BODY_ACTION__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setBodyAction(ActionUsage newBodyAction) {
		BODY_ACTION__ESETTING_DELEGATE.dynamicSet(this, null, 0, newBodyAction);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.LOOP_ACTION_USAGE__BODY_ACTION:
				if (resolve) return getBodyAction();
				return basicGetBodyAction();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case SysMLPackage.LOOP_ACTION_USAGE__BODY_ACTION:
				setBodyAction((ActionUsage)newValue);
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
			case SysMLPackage.LOOP_ACTION_USAGE__BODY_ACTION:
				setBodyAction((ActionUsage)null);
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
			case SysMLPackage.LOOP_ACTION_USAGE__BODY_ACTION:
				return BODY_ACTION__ESETTING_DELEGATE.dynamicIsSet(this, null, 0);
		}
		return super.eIsSet(featureID);
	}

} //LoopActionUsageImpl

````
