# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationDefinitionImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationDefinitionImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationDefinitionImpl.java
- source_bytes: 4162
- source_sha256: `b73c67c07f78223eda49ca272bcfc105bffaefaf1a63106b1c2ca6d52b7ee7f8`
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

import org.omg.sysml.lang.sysml.EnumerationDefinition;
import org.omg.sysml.lang.sysml.EnumerationUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.Usage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Enumeration Definition</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.EnumerationDefinitionImpl#getEnumeratedValue <em>Enumerated Value</em>}</li>
 * </ul>
 *
 * @generated
 */
public class EnumerationDefinitionImpl extends AttributeDefinitionImpl implements EnumerationDefinition {
	/**
	 * The cached setting delegate for the '{@link #getEnumeratedValue() <em>Enumerated Value</em>}' reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getEnumeratedValue()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate ENUMERATED_VALUE__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.ENUMERATION_DEFINITION__ENUMERATED_VALUE).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated NOT
	 */
	protected EnumerationDefinitionImpl() {
		super();
		isVariation = IS_VARIATION_EDEFAULT = true;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.ENUMERATION_DEFINITION;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public EList<EnumerationUsage> getEnumeratedValue() {
		return (EList<EnumerationUsage>)ENUMERATED_VALUE__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetEnumeratedValue() {
		return !getEnumeratedValue().isEmpty();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.ENUMERATION_DEFINITION__ENUMERATED_VALUE:
				return getEnumeratedValue();
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
			case SysMLPackage.ENUMERATION_DEFINITION__ENUMERATED_VALUE:
				getEnumeratedValue().clear();
				getEnumeratedValue().addAll((Collection<? extends EnumerationUsage>)newValue);
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
			case SysMLPackage.ENUMERATION_DEFINITION__ENUMERATED_VALUE:
				getEnumeratedValue().clear();
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
			case SysMLPackage.ENUMERATION_DEFINITION__VARIANT:
				return isSetVariant();
			case SysMLPackage.ENUMERATION_DEFINITION__ENUMERATED_VALUE:
				return isSetEnumeratedValue();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EList<Usage> getVariant() {
		@SuppressWarnings("unchecked")
		EList<Usage> enumeratedValue = (EList<Usage>)((EList<?>)getEnumeratedValue());
		return enumeratedValue;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetVariant() {
  		return false;
	}

} //EnumerationDefinitionImpl

````
