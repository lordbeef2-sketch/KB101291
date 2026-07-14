# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/RequirementConstraintMembershipItemProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/RequirementConstraintMembershipItemProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.edit/src/org/omg/sysml/lang/sysml/provider/RequirementConstraintMembershipItemProvider.java
- source_bytes: 6871
- source_sha256: `aeb2b550417e9afcbf7659df0e91e7b9b08b88910d5e88527959607c7d7a7071`
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
import org.eclipse.emf.edit.provider.ItemPropertyDescriptor;
import org.eclipse.emf.edit.provider.ViewerNotification;

import org.omg.sysml.lang.sysml.RequirementConstraintMembership;
import org.omg.sysml.lang.sysml.SysMLPackage;

/**
 * This is the item provider adapter for a {@link org.omg.sysml.lang.sysml.RequirementConstraintMembership} object.
 * <!-- begin-user-doc -->
 * <!-- end-user-doc -->
 * @generated
 */
public class RequirementConstraintMembershipItemProvider extends FeatureMembershipItemProvider {
	/**
	 * This constructs an instance from a factory and a notifier.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public RequirementConstraintMembershipItemProvider(AdapterFactory adapterFactory) {
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

			addKindPropertyDescriptor(object);
			addOwnedConstraintPropertyDescriptor(object);
			addReferencedConstraintPropertyDescriptor(object);
		}
		return itemPropertyDescriptors;
	}

	/**
	 * This adds a property descriptor for the Kind feature.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected void addKindPropertyDescriptor(Object object) {
		itemPropertyDescriptors.add
			(createItemPropertyDescriptor
				(((ComposeableAdapterFactory)adapterFactory).getRootAdapterFactory(),
				 getResourceLocator(),
				 getString("_UI_RequirementConstraintMembership_kind_feature"),
				 getString("_UI_PropertyDescriptor_description", "_UI_RequirementConstraintMembership_kind_feature", "_UI_RequirementConstraintMembership_type"),
				 SysMLPackage.Literals.REQUIREMENT_CONSTRAINT_MEMBERSHIP__KIND,
				 true,
				 false,
				 false,
				 ItemPropertyDescriptor.GENERIC_VALUE_IMAGE,
				 null,
				 null));
	}

	/**
	 * This adds a property descriptor for the Owned Constraint feature.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected void addOwnedConstraintPropertyDescriptor(Object object) {
		itemPropertyDescriptors.add
			(createItemPropertyDescriptor
				(((ComposeableAdapterFactory)adapterFactory).getRootAdapterFactory(),
				 getResourceLocator(),
				 getString("_UI_RequirementConstraintMembership_ownedConstraint_feature"),
				 getString("_UI_PropertyDescriptor_description", "_UI_RequirementConstraintMembership_ownedConstraint_feature", "_UI_RequirementConstraintMembership_type"),
				 SysMLPackage.Literals.REQUIREMENT_CONSTRAINT_MEMBERSHIP__OWNED_CONSTRAINT,
				 true,
				 false,
				 true,
				 null,
				 null,
				 null));
	}

	/**
	 * This adds a property descriptor for the Referenced Constraint feature.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected void addReferencedConstraintPropertyDescriptor(Object object) {
		itemPropertyDescriptors.add
			(createItemPropertyDescriptor
				(((ComposeableAdapterFactory)adapterFactory).getRootAdapterFactory(),
				 getResourceLocator(),
				 getString("_UI_RequirementConstraintMembership_referencedConstraint_feature"),
				 getString("_UI_PropertyDescriptor_description", "_UI_RequirementConstraintMembership_referencedConstraint_feature", "_UI_RequirementConstraintMembership_type"),
				 SysMLPackage.Literals.REQUIREMENT_CONSTRAINT_MEMBERSHIP__REFERENCED_CONSTRAINT,
				 true,
				 false,
				 true,
				 null,
				 null,
				 null));
	}

	/**
	 * This returns RequirementConstraintMembership.gif.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object getImage(Object object) {
		return overlayImage(object, getResourceLocator().getImage("full/obj16/RequirementConstraintMembership"));
	}

	/**
	 * This returns the label text for the adapted class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String getText(Object object) {
		String label = ((RequirementConstraintMembership)object).getName();
		return label == null || label.length() == 0 ?
			getString("_UI_RequirementConstraintMembership_type") :
			getString("_UI_RequirementConstraintMembership_type") + " " + label;
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

		switch (notification.getFeatureID(RequirementConstraintMembership.class)) {
			case SysMLPackage.REQUIREMENT_CONSTRAINT_MEMBERSHIP__KIND:
				fireNotifyChanged(new ViewerNotification(notification, notification.getNotifier(), false, true));
				return;
		}
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
			childFeature == SysMLPackage.Literals.RELATIONSHIP__OWNED_RELATED_ELEMENT ||
			childFeature == SysMLPackage.Literals.OWNING_MEMBERSHIP__OWNED_MEMBER_ELEMENT ||
			childFeature == SysMLPackage.Literals.ELEMENT__OWNED_ANNOTATION;

		if (qualify) {
			return getString
				("_UI_CreateChild_text2",
				 new Object[] { getTypeText(childObject), getFeatureText(childFeature), getTypeText(owner) });
		}
		return super.getCreateChildText(owner, feature, child, selection);
	}

}

````
