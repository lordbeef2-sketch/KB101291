# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PartUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PartUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PartUsage.java
- source_bytes: 2952
- source_sha256: `de63cc6a21011be9c4660bc47a1a5f3930c5bf51c3b0eb0701277b8153870d40`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Part Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>PartUsage</code> is a usage of a <code>PartDefinition</code> to represent a system or a part of a system. At least one of the <code>itemDefinitions</code> of the <code>PartUsage</code> must be a <code>PartDefinition</code>.</p>
 * 
 * <p>A <code>PartUsage</code> must subset, directly or indirectly, the base <code>PartUsage</code> <em><code>parts</code></em> from the Systems Model Library.</p>
 * itemDefinition->selectByKind(PartDefinition)
 * partDefinition->notEmpty()
 * specializesFromLibrary('Parts::parts')
 * isComposite and owningType <> null and
 * (owningType.oclIsKindOf(ItemDefinition) or
 *  owningType.oclIsKindOf(ItemUsage)) implies
 *     specializesFromLibrary('Items::Item::subparts')
 * owningFeatureMembership <> null and
 * owningFeatureMembership.oclIsKindOf(ActorMembership) implies
 *     if owningType.oclIsKindOf(RequirementDefinition) or 
 *        owningType.oclIsKindOf(RequirementUsage)
 *     then specializesFromLibrary('Requirements::RequirementCheck::actors')
 *     else specializesFromLibrary('Cases::Case::actors')
 * owningFeatureMembership <> null and
 * owningFeatureMembership.oclIsKindOf(StakeholderMembership) implies
 *     specializesFromLibrary('Requirements::RequirementCheck::stakeholders')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.PartUsage#getPartDefinition <em>Part Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPartUsage()
 * @model
 * @generated
 */
public interface PartUsage extends ItemUsage {
	/**
	 * Returns the value of the '<em><b>Part Definition</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.PartDefinition}.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.ItemUsage#getItemDefinition() <em>Item Definition</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>itemDefinitions</code> of this PartUsage that are PartDefinitions.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Part Definition</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPartUsage_PartDefinition()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='definedPart'"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<PartDefinition> getPartDefinition();

} // PartUsage

````
