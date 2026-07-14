# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationUsageImpl.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationUsageImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/impl/EnumerationUsageImpl.java
- source_bytes: 5053
- source_sha256: `c4ea6b7c15c9457c8a387acf3aa0ba793c08573f2187523c172cf01c15ca42b4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml.impl;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.common.util.UniqueEList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.omg.sysml.lang.sysml.util.UnionEObjectEList;
import org.omg.sysml.lang.sysml.DataType;
import org.omg.sysml.lang.sysml.EnumerationDefinition;
import org.omg.sysml.lang.sysml.EnumerationUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Enumeration Usage</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.impl.EnumerationUsageImpl#getEnumerationDefinition <em>Enumeration Definition</em>}</li>
 * </ul>
 *
 * @generated
 */
public class EnumerationUsageImpl extends AttributeUsageImpl implements EnumerationUsage {
	/**
	 * The cached setting delegate for the '{@link #getEnumerationDefinition() <em>Enumeration Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getEnumerationDefinition()
	 * @generated
	 * @ordered
	 */
	protected EStructuralFeature.Internal.SettingDelegate ENUMERATION_DEFINITION__ESETTING_DELEGATE = ((EStructuralFeature.Internal)SysMLPackage.Literals.ENUMERATION_USAGE__ENUMERATION_DEFINITION).getSettingDelegate();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected EnumerationUsageImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return SysMLPackage.Literals.ENUMERATION_USAGE;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EnumerationDefinition getEnumerationDefinition() {
		return (EnumerationDefinition)ENUMERATION_DEFINITION__ESETTING_DELEGATE.dynamicGet(this, null, 0, true, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EnumerationDefinition basicGetEnumerationDefinition() {
		return (EnumerationDefinition)ENUMERATION_DEFINITION__ESETTING_DELEGATE.dynamicGet(this, null, 0, false, false);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void setEnumerationDefinition(EnumerationDefinition newEnumerationDefinition) {
		ENUMERATION_DEFINITION__ESETTING_DELEGATE.dynamicSet(this, null, 0, newEnumerationDefinition);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetEnumerationDefinition() {
		return basicGetEnumerationDefinition() != null;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case SysMLPackage.ENUMERATION_USAGE__ENUMERATION_DEFINITION:
				if (resolve) return getEnumerationDefinition();
				return basicGetEnumerationDefinition();
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
			case SysMLPackage.ENUMERATION_USAGE__ENUMERATION_DEFINITION:
				setEnumerationDefinition((EnumerationDefinition)newValue);
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
			case SysMLPackage.ENUMERATION_USAGE__ENUMERATION_DEFINITION:
				setEnumerationDefinition((EnumerationDefinition)null);
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
			case SysMLPackage.ENUMERATION_USAGE__ATTRIBUTE_DEFINITION:
				return isSetAttributeDefinition();
			case SysMLPackage.ENUMERATION_USAGE__ENUMERATION_DEFINITION:
				return isSetEnumerationDefinition();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EList<DataType> getAttributeDefinition() {
		EList<DataType> attributeDefinition = new UniqueEList<DataType>();
		EnumerationDefinition enumerationDefinition = getEnumerationDefinition();
		if (enumerationDefinition != null) {
			attributeDefinition.add(enumerationDefinition);
		}
		return new UnionEObjectEList<DataType>(this, SysMLPackage.Literals.ATTRIBUTE_USAGE__ATTRIBUTE_DEFINITION, attributeDefinition.size(), attributeDefinition.toArray());
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public boolean isSetAttributeDefinition() {
  		return false;
	}

} //EnumerationUsageImpl

````
