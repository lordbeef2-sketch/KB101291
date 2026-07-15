# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FeatureChainExpression.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FeatureChainExpression.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/FeatureChainExpression.java
- source_bytes: 4406
- source_sha256: `e7474cc07966c91c5b91dc82c3cdafed4503ae017ace68ae6911a973b5782d1c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Feature Chain Expression</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>FeatureChainExpression</code> is an <code>OperatorExpression</code> whose operator is <code>"."</code>, which resolves to the <code>Function</code> <em><code>ControlFunctions::'.'</code></em> from the Kernel Functions Library. It evaluates to the result of chaining the <code>result</code> <code>Feature</code> of its single <code>argument</code> <code>Expression</code> with its <code>targetFeature</code>.</p>
 * let sourceTargetFeature : Feature = sourceTargetFeature() in
 * sourceTargetFeature <> null and
 * sourceTargetFeature.redefinesFromLibrary('ControlFunctions::\'.\'::source::target')
 * let sourceTargetFeature : Feature = sourceTargetFeature() in
 * sourceTargetFeature <> null and
 * sourceTargetFeature.redefines(targetFeature)
 * targetFeature =
 *     let nonParameterMemberships : Sequence(Membership) = ownedMembership->
 *         reject(oclIsKindOf(ParameterMembership)) in
 *     if nonParameterMemberships->isEmpty() or
 *        not nonParameterMemberships->first().memberElement.oclIsKindOf(Feature)
 *     then null
 *     else nonParameterMemberships->first().memberElement.oclAsType(Feature)
 *     endif
 * argument->notEmpty() implies
 *     targetFeature.isFeaturedWithin(argument->first().result)
 * operator = '.'
 * let inputParameters : Sequence(Feature) = 
 *     ownedFeatures->select(direction = _'in') in
 * let sourceTargetFeature : Feature = 
 *     owningExpression.sourceTargetFeature() in
 * sourceTargetFeature <> null and
 * result.subsetsChain(inputParameters->first(), sourceTargetFeature) and
 * result.owningType = self
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.FeatureChainExpression#getTargetFeature <em>Target Feature</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getFeatureChainExpression()
 * @model
 * @generated
 */
public interface FeatureChainExpression extends OperatorExpression {
	/**
	 * Returns the value of the '<em><b>Target Feature</b></em>' reference.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Namespace#getMember() <em>Member</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Feature</code> that is accessed by this <code>FeatureChainExpression<code>, which is its first non-<code>parameter</code> <code>member</code>.<p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Target Feature</em>' reference.
	 * @see #setTargetFeature(Feature)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getFeatureChainExpression_TargetFeature()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='chainExpression'"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Feature getTargetFeature();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.FeatureChainExpression#getTargetFeature <em>Target Feature</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Target Feature</em>' reference.
	 * @see #getTargetFeature()
	 * @generated
	 */
	void setTargetFeature(Feature value);

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Return the first <code>ownedFeature</code> of the first owned input <code>parameter</code> of this <code>FeatureChainExpression</code> (if any).</p>
	 * let inputParameters : Feature = ownedFeatures->
	 *     select(direction = _'in') in
	 * if inputParameters->isEmpty() or 
	 *    inputParameters->first().ownedFeature->isEmpty()
	 * then null
	 * else inputParameters->first().ownedFeature->first()
	 * endif
	 * <!-- end-model-doc -->
	 * @model ordered="false"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Feature sourceTargetFeature();

} // FeatureChainExpression

````
