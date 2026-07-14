# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/WhileLoopActionUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/WhileLoopActionUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/WhileLoopActionUsage.java
- source_bytes: 4675
- source_sha256: `766b605bee5da4f41078e387d5e83e89f0f0943bdbae5882b9df5bfa58bd44b8`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>While Loop Action Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>WhileLoopActionUsage</code> is a <code>LoopActionUsage</code> that specifies that the <code>bodyAction</code> <code>ActionUsage</code> should be performed repeatedly while the result of the <code>whileArgument</code> <code>Expression</code> is true or until the result of the <code>untilArgument</code> <code>Expression</code> (if provided) is true. The <code>whileArgument</code> <code>Expression</code> is evaluated before each (possible) performance of the <code>bodyAction</code>, and the <code>untilArgument</code> <code>Expression</code> is evaluated after each performance of the <code>bodyAction</code>.</p>
 * isSubactionUsage() implies
 *     specializesFromLibrary('Actions::Action::whileLoops')
 * untilArgument =
 *     let parameter : Feature = inputParameter(3) in
 *     if parameter <> null and parameter.oclIsKindOf(Expression) then
 *         parameter.oclAsType(Expression)
 *     else
 *         null
 *     endif
 * 
 * specializesFromLibrary('Actions::whileLoopActions')
 * whileArgument =
 *     let parameter : Feature = inputParameter(1) in
 *     if parameter <> null and parameter.oclIsKindOf(Expression) then
 *         parameter.oclAsType(Expression)
 *     else
 *         null
 *     endif
 * 
 * inputParameters()->size() >= 2
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.WhileLoopActionUsage#getUntilArgument <em>Until Argument</em>}</li>
 *   <li>{@link org.omg.sysml.lang.sysml.WhileLoopActionUsage#getWhileArgument <em>While Argument</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getWhileLoopActionUsage()
 * @model
 * @generated
 */
public interface WhileLoopActionUsage extends LoopActionUsage {
	/**
	 * Returns the value of the '<em><b>While Argument</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Expression</code> whose result, if true, determines that the <code>bodyAction</code> should continue to be performed. It is the first owned <code>parameter</code> of the <code>WhileLoopActionUsage</code>.</p> 
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>While Argument</em>' reference.
	 * @see #setWhileArgument(Expression)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getWhileLoopActionUsage_WhileArgument()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='whileLoopAction'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Expression getWhileArgument();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.WhileLoopActionUsage#getWhileArgument <em>While Argument</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>While Argument</em>' reference.
	 * @see #getWhileArgument()
	 * @generated
	 */
	void setWhileArgument(Expression value);

	/**
	 * Returns the value of the '<em><b>Until Argument</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Expression</code> whose result, if false, determines that the <code>bodyAction</code> should continue to be performed. It is the (optional) third owned <code>parameter</code> of the <code>WhileLoopActionUsage</code>.</p> 
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Until Argument</em>' reference.
	 * @see #setUntilArgument(Expression)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getWhileLoopActionUsage_UntilArgument()
	 * @model transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='untilLoopAction'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Expression getUntilArgument();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.WhileLoopActionUsage#getUntilArgument <em>Until Argument</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Until Argument</em>' reference.
	 * @see #getUntilArgument()
	 * @generated
	 */
	void setUntilArgument(Expression value);

} // WhileLoopActionUsage

````
