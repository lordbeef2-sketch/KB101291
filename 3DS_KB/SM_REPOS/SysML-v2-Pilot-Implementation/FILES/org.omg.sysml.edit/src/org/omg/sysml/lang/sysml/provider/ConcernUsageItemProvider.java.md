# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/ConcernUsageItemProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/ConcernUsageItemProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/ConcernUsageItemProvider.java
- source_bytes: 5172
- source_sha256: `07d4d9d4a6e52889904a83c531e00ae1230f00f6cccbf158371e57da32967122`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml.provider;


import java.util.Collection;
import java.util.List;

import org.eclipse.emf.common.notify.AdapterFactory;
import org.eclipse.emf.common.notify.Notification;

import org.eclipse.emf.edit.provider.ComposeableAdapterFactory;
import org.eclipse.emf.edit.provider.IItemPropertyDescriptor;

import org.omg.sysml.lang.sysml.ConcernUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;

/**
 * This is the item provider adapter for a {@link org.omg.sysml.lang.sysml.ConcernUsage} object.
 * <!-- begin-user-doc -->
 * <!-- end-user-doc -->
 * @generated
 */
public class ConcernUsageItemProvider extends RequirementUsageItemProvider {
	/**
	 * This constructs an instance from a factory and a notifier.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public ConcernUsageItemProvider(AdapterFactory adapterFactory) {
		super(adapterFactory);
	}

	/**
	 * This returns the property descriptors for the adapted class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public List<IItemPropertyDescriptor> getPropertyDescriptors(Object object) {
		if (itemPropertyDescriptors == null) {
			super.getPropertyDescriptors(object);

			addConcernDefinitionPropertyDescriptor(object);
		}
		return itemPropertyDescriptors;
	}

	/**
	 * This adds a property descriptor for the Concern Definition feature.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected void addConcernDefinitionPropertyDescriptor(Object object) {
		itemPropertyDescriptors.add
			(createItemPropertyDescriptor
				(((ComposeableAdapterFactory)adapterFactory).getRootAdapterFactory(),
				 getResourceLocator(),
				 getString("_UI_ConcernUsage_concernDefinition_feature"),
				 getString("_UI_PropertyDescriptor_description", "_UI_ConcernUsage_concernDefinition_feature", "_UI_ConcernUsage_type"),
				 SysMLPackage.Literals.CONCERN_USAGE__CONCERN_DEFINITION,
				 true,
				 false,
				 true,
				 null,
				 null,
				 null));
	}

	/**
	 * This returns ConcernUsage.gif.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object getImage(Object object) {
		return overlayImage(object, getResourceLocator().getImage("full/obj16/ConcernUsage"));
	}

	/**
	 * This returns the label text for the adapted class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getText(Object object) {
		String label = ((ConcernUsage)object).getName();
		return label == null || label.length() == 0 ?
			getString("_UI_ConcernUsage_type") :
			getString("_UI_ConcernUsage_type") + " " + label;
	}


	/**
	 * This handles model notifications by calling {@link #updateChildren} to update any cached
	 * children and by creating a viewer notification, which it passes to {@link #fireNotifyChanged}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void notifyChanged(Notification notification) {
		updateChildren(notification);
		super.notifyChanged(notification);
	}

	/**
	 * This adds {@link org.eclipse.emf.edit.command.CommandParameter}s describing the children
	 * that can be created under this object.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected void collectNewChildDescriptors(Collection<Object> newChildDescriptors, Object object) {
		super.collectNewChildDescriptors(newChildDescriptors, object);
	}

	/**
	 * This returns the label text for {@link org.eclipse.emf.edit.command.CreateChildCommand}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getCreateChildText(Object owner, Object feature, Object child, Collection<?> selection) {
		Object childFeature = feature;
		Object childObject = child;

		boolean qualify =
			childFeature == SysMLPackage.Literals.ELEMENT__OWNED_RELATIONSHIP ||
			childFeature == SysMLPackage.Literals.NAMESPACE__OWNED_MEMBERSHIP ||
			childFeature == SysMLPackage.Literals.ELEMENT__OWNED_ANNOTATION ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_SPECIALIZATION ||
			childFeature == SysMLPackage.Literals.FEATURE__OWNED_TYPE_FEATURING ||
			childFeature == SysMLPackage.Literals.FEATURE__OWNED_FEATURE_INVERTING ||
			childFeature == SysMLPackage.Literals.FEATURE__OWNED_FEATURE_CHAINING ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_CONJUGATOR ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_INTERSECTING ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_UNIONING ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_DISJOINING ||
			childFeature == SysMLPackage.Literals.TYPE__OWNED_DIFFERENCING ||
			childFeature == SysMLPackage.Literals.NAMESPACE__OWNED_IMPORT;

		if (qualify) {
			return getString
				("_UI_CreateChild_text2",
				 new Object[] { getTypeText(childObject), getFeatureText(childFeature), getTypeText(owner) });
		}
		return super.getCreateChildText(owner, feature, child, selection);
	}

}

````
