# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/IndexExpression.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/IndexExpression.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/IndexExpression.java
- source_bytes: 866
- source_sha256: `6e3a3b88355f72e0632e4a9a35186a91fba604d1dab1bc6f9adc8a6400ca4b51`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Index Expression</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>IndexExpression</code> is an <code>OperatorExpression</code> whose operator is <code>"#"</code>, which resolves to the <code>Function</code> <em><code>BasicFunctions::'#'</code></em> from the Kernel Functions Library.</p>
 * arguments->notEmpty() and 
 * not arguments->first().result.specializesFromLibrary('Collections::Array') implies
 *     result.specializes(arguments->first().result)
 * operator = '#'
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getIndexExpression()
 * @model
 * @generated
 */
public interface IndexExpression extends OperatorExpression {
} // IndexExpression

````
