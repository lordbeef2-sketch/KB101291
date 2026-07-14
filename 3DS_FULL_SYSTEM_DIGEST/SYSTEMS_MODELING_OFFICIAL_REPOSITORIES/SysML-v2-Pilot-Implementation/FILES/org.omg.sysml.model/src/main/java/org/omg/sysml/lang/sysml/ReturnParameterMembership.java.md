# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReturnParameterMembership.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReturnParameterMembership.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReturnParameterMembership.java
- source_bytes: 906
- source_sha256: `a4d621705c026f76f4404a48b8c306bdf236006ade2122c349099421c26b5130`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Return Parameter Membership</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ReturnParameterMembership</code> is a <code>ParameterMembership</code> that indicates that the <code>ownedMemberParameter</code> is the <code>result</code> <code>parameter</code> of a <code>Function</code> or <code>Expression</code>. The <code>direction</code> of the <code>ownedMemberParameter</code> must be <code>out</code>.</p>
 * 
 * owningType.oclIsKindOf(Function) or owningType.oclIsKindOf(Expression)
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getReturnParameterMembership()
 * @model
 * @generated
 */
public interface ReturnParameterMembership extends ParameterMembership {
} // ReturnParameterMembership

````
