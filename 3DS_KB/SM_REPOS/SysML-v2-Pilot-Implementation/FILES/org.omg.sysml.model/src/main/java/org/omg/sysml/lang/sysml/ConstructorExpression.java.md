# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConstructorExpression.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConstructorExpression.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ConstructorExpression.java
- source_bytes: 1764
- source_sha256: `59abe5fe0487134e4f52c4c6c21340456275eccd81f56322dbbfb47590396e16`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Constructor Expression</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ConstructorExpression</code> is an <code>InstantiationExpression</code> whose <code>result</code> specializes its <code>instantiatedType</code>, binding some or all of the <code>features</code> of the <code>instantiatedType</code> to the <code>results</code> of its <code>argument</code> <code>Expressions</code>.</p>
 * instantiatedType.feature->collect(f | 
 *     result.ownedFeatures->select(redefines(f)).valuation->
 *     select(v | v <> null).value
 * )
 * let features : OrderedSet(Feature) = instantiatedType.feature->
 *     select(visibility = VisibilityKind::public) in
 * result.ownedFeature->forAll(f1 | result.ownedFeature->forAll(f2 |
 *     f1 <> f2 implies
 *         f1.ownedRedefinition.redefinedFeature->
 *             intersection(f2.ownedRedefinition.redefinedFeature)->
 *             intersection(features)->isEmpty()))
 * let features : OrderedSet(Feature) = instantiatedType.feature->
 *     select(owningMembership.visibility = VisibilityKind::public) in
 * result.ownedFeature->forAll(f | 
 *     f.ownedRedefinition.redefinedFeature->
 *         intersection(features)->size() = 1)
 * TBD
 * specializes('Performances::constructorEvaluations')
 * result.specializes(instantiatedType)
 * ownedFeatures->excluding(result)->isEmpty()
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getConstructorExpression()
 * @model
 * @generated
 */
public interface ConstructorExpression extends InstantiationExpression {
} // ConstructorExpression

````
