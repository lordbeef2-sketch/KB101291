# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SelectExpression.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SelectExpression.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/SelectExpression.java
- source_bytes: 801
- source_sha256: `1d3921b56e1dbbd8deee9f9e795e20010eaf611289336bfad9569fda6f0f34c3`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Select Expression</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>SelectExpression</code> is an <code>OperatorExpression</code> whose operator is <code>"select"</code>, which resolves to the <code>Function</code> <em><code>ControlFunctions::select</code></em> from the Kernel Functions Library.</p>
 * operator = 'select'
 * arguments->notEmpty() implies
 *     result.specializes(arguments->first().result)
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getSelectExpression()
 * @model
 * @generated
 */
public interface SelectExpression extends OperatorExpression {
} // SelectExpression

````
