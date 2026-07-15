# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Package.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Package.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Package.java
- source_bytes: 3044
- source_sha256: `637f99b114e588d30a8ba1cb80ad7efff606c279b8ec0539625d4e8f353a9022`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Package</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>Package</code> is a <code>Namespace</code> used to group <code>Elements</code>, without any instance-level semantics. It may have one or more model-level evaluable <code>filterCondition</code> <code>Expressions</code> used to filter its <code>importedMemberships</code>. Any imported <code>member</code> must meet all of the <code>filterConditions</code>.</p>
 * filterCondition = ownedMembership->
 *     selectByKind(ElementFilterMembership).condition
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Package#getFilterCondition <em>Filter Condition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPackage()
 * @model
 * @generated
 */
public interface Package extends Namespace {
	/**
	 * Returns the value of the '<em><b>Filter Condition</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.Expression}.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Namespace#getOwnedMember() <em>Owned Member</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The model-level evaluable <code><em>Boolean</em></code>-valued <code>Expression</code> used to filter the <code>members</code> of this <code>Package</code>, which are owned by the <code>Package</code> are via <code>ElementFilterMemberships</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Filter Condition</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPackage_FilterCondition()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='conditionedPackage'"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<Expression> getFilterCondition();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Determine whether the given <code>element</code> meets all the <code>filterConditions</code>.</p>
	 * let metadataFeatures: Sequence(AnnotatingElement) = 
	 *     element.ownedAnnotation.annotatingElement->
	 *         selectByKind(MetadataFeature) in
	 *     self.filterCondition->forAll(cond | 
	 *         metadataFeatures->exists(elem | 
	 *             cond.checkCondition(elem)))
	 * <!-- end-model-doc -->
	 * @model required="true" ordered="false" elementRequired="true" elementOrdered="false"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	boolean includeAsMember(Element element);

} // Package

````
