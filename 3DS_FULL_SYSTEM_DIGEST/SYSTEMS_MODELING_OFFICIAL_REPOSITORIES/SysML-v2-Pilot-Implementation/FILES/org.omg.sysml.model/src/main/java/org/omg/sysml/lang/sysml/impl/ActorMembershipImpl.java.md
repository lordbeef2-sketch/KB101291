# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ActorMembershipImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ActorMembershipImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/ActorMembershipImpl.java
- source_bytes: 4997
- source_sha256: `8c1a8579d19efdc8d2285ec0ebfbc7e69ce4508d764a6b4e66e7355dee5e2c3b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml.impl;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;

import org.omg.sysml.lang.sysml.ActorMembership;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.PartUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Actor Membership</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.ActorMembershipImpl#getOwnedActorParameter <em>Owned Actor Parameter</em>}</li>
 * </ul>
 *
 * @generated
 */
public class ActorMembershipImpl extends ParameterMembershipImpl implements ActorMembership {
	/**
	 * The cached setting delegate for the '{@link #getOwnedActorParameter() <em>Owned Actor Parameter</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getOwnedActorParameter()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate OWNED_ACTOR_PARAMETER__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.ACTOR_MEMBERSHIP__OWNED_ACTOR_PARAMETER).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ActorMembershipImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.ACTOR_MEMBERSHIP;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public PartUsage getOwnedActorParameter() {
		return (PartUsage)OWNED_ACTOR_PARAMETER__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public PartUsage basicGetOwnedActorParameter() {
		return (PartUsage)OWNED_ACTOR_PARAMETER__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setOwnedActorParameter(PartUsage newOwnedActorParameter) {
		OWNED_ACTOR_PARAMETER__ESETTING_DELEGATE.dynamicSet(this, null, 0, newOwnedActorParameter);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetOwnedActorParameter() {
		return basicGetOwnedActorParameter() != null;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.ACTOR_MEMBERSHIP__OWNED_ACTOR_PARAMETER:
				if (resolve) return getOwnedActorParameter();
				return basicGetOwnedActorParameter();
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
			case SysMLPackage.ACTOR_MEMBERSHIP__OWNED_ACTOR_PARAMETER:
				setOwnedActorParameter((PartUsage)newValue);
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
			case SysMLPackage.ACTOR_MEMBERSHIP__OWNED_ACTOR_PARAMETER:
				setOwnedActorParameter((PartUsage)null);
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
			case SysMLPackage.ACTOR_MEMBERSHIP__OWNED_MEMBER_PARAMETER:
				return isSetOwnedMemberParameter();
			case SysMLPackage.ACTOR_MEMBERSHIP__OWNED_ACTOR_PARAMETER:
				return isSetOwnedActorParameter();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Feature getOwnedMemberParameter() {
		return getOwnedActorParameter();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Feature basicGetOwnedMemberParameter() {
		return basicGetOwnedActorParameter();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setOwnedMemberParameter(Feature newOwnedMemberParameter) {
		if (newOwnedMemberParameter != null && !(newOwnedMemberParameter instanceof PartUsage)) {
			throw new IllegalArgumentException("newOwnedMemberParameter must be an instance of PartUsage");
		}
		setOwnedActorParameter((PartUsage) newOwnedMemberParameter);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetOwnedMemberParameter() {
  		return false;
	}

} //ActorMembershipImpl

````
