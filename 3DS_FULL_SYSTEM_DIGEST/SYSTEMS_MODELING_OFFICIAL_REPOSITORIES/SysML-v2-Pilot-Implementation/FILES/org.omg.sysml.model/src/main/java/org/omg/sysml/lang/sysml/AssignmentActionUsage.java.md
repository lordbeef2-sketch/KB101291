# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssignmentActionUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssignmentActionUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssignmentActionUsage.java
- source_bytes: 6940
- source_sha256: `2fd3461a28a204999d99ac4e920ba7778c16e66cd5c8396d6cb8c986ccb825f5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Assignment Action Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>AssignmentActionUsage</code> is an <code>ActionUsage</code> that is defined, directly or indirectly, by the <code>ActionDefinition</code> <em><code>AssignmentAction</code></em> from the Systems Model Library. It specifies that the value of the <code>referent</code> <code>Feature</code>, relative to the target given by the result of the <code>targetArgument</code> <code>Expression</code>, should be set to the result of the <code>valueExpression</code>.</p>
 * 
 * specializesFromLibrary('Actions::assignmentActions')
 * let targetParameter : Feature = inputParameter(1) in
 * targetParameter <> null and
 * targetParameter.ownedFeature->notEmpty() and
 * targetParameter.ownedFeature->first().
 *     redefinesFromLibrary('AssignmentAction::target::startingAt')
 * valueExpression = argument(2)
 * targetArgument = argument(1)
 * isSubactionUsage() implies
 *     specializesFromLibrary('Actions::Action::assignments')
 * let targetParameter : Feature = inputParameter(1) in
 * targetParameter <> null and
 * targetParameter.ownedFeature->notEmpty() and
 * targetParameter.ownedFeature->first().ownedFeature->notEmpty() and
 * targetParameter.ownedFeature->first().ownedFeature->first().
 *     redefinesFromLibrary('AssigmentAction::target::startingAt::accessedFeature')
 * let targetParameter : Feature = inputParameter(1) in
 * targetParameter <> null and
 * targetParameter.ownedFeature->notEmpty() and
 * targetParameter.ownedFeature->first().ownedFeature->notEmpty() and
 * targetParameter.ownedFeature->first().ownedFeature->first().redefines(referent)
 * referent =
 *     let unownedFeatures : Sequence(Feature) = ownedMembership->
 *         reject(oclIsKindOf(FeatureMembership)).memberElement->
 *         select(oclIsKindOf(Feature) and 
 *                not oclIsKindOf(MetadataFeature)) in
 *     if unownedFeatures->isEmpty() then null
 *     else unownedFeatures->first().oclAsType(Feature)
 *     endif
 * ownedMembership->exists(
 *     not oclIsKindOf(OwningMembership) and 
 *     memberElement.oclIsKindOf(Feature) and
 *     not memberElement.oclIsKindOf(MetadataFeature))
 * referent <> null implies referent.featureTarget.isVariable
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getReferent <em>Referent</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getTargetArgument <em>Target Argument</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getValueExpression <em>Value Expression</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getAssignmentActionUsage()
 * @model
 * @generated
 */
public interface AssignmentActionUsage extends ActionUsage {
	/**
	 * Returns the value of the '<em><b>Target Argument</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Expression</code> whose value is an occurrence in the domain of the <code>referent</code> <code>Feature</code>, for which the value of the <code>referent</code> will be set to the result of the <code>valueExpression</code> by this <code>AssignmentActionUsage</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Target Argument</em>' reference.
	 * @see #setTargetArgument(Expression)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getAssignmentActionUsage_TargetArgument()
	 * @model transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='assignmentAction'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Expression getTargetArgument();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getTargetArgument <em>Target Argument</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Target Argument</em>' reference.
	 * @see #getTargetArgument()
	 * @generated
	 */
	void setTargetArgument(Expression value);

	/**
	 * Returns the value of the '<em><b>Value Expression</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Expression</code> whose result is to be assigned to the <code>referent</code> <code>Feature</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Value Expression</em>' reference.
	 * @see #setValueExpression(Expression)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getAssignmentActionUsage_ValueExpression()
	 * @model transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='assigningAction'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Expression getValueExpression();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getValueExpression <em>Value Expression</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Value Expression</em>' reference.
	 * @see #getValueExpression()
	 * @generated
	 */
	void setValueExpression(Expression value);

	/**
	 * Returns the value of the '<em><b>Referent</b></em>' reference.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Namespace#getMember() <em>Member</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Feature</code> whose value is to be set.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Referent</em>' reference.
	 * @see #setReferent(Feature)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getAssignmentActionUsage_Referent()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='assignment'"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Feature getReferent();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.AssignmentActionUsage#getReferent <em>Referent</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Referent</em>' reference.
	 * @see #getReferent()
	 * @generated
	 */
	void setReferent(Feature value);

} // AssignmentActionUsage

````
