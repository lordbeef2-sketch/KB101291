# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LoopActionUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LoopActionUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/LoopActionUsage.java
- source_bytes: 2419
- source_sha256: `2ed4a2d0f73ca16147de73977e56ac8788e95be0f81e9d52060c225f41d313f3`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Loop Action Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>LoopActionUsage</code> is an <code>ActionUsage</code> that specifies that its <code>bodyAction</code> should be performed repeatedly. Its subclasses <code>WhileLoopActionUsage</code> and <code>ForLoopActionUsage</code> provide different ways to determine how many times the <code>bodyAction</code> should be performed.</p>
 * bodyAction =
 *     let parameter : Feature = inputParameter(2) in
 *     if parameter <> null and parameter.oclIsKindOf(Action) then
 *         parameter.oclAsType(Action)
 *     else
 *         null
 *     endif
 * 
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.LoopActionUsage#getBodyAction <em>Body Action</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getLoopActionUsage()
 * @model abstract="true"
 * @generated
 */
public interface LoopActionUsage extends ActionUsage {
	/**
	 * Returns the value of the '<em><b>Body Action</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>ActionUsage</code> to be performed repeatedly by the <code>LoopActionUsage</code>. It is the second <code>parameter</code> of the <code>LoopActionUsage</code>.</p> 
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Body Action</em>' reference.
	 * @see #setBodyAction(ActionUsage)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getLoopActionUsage_BodyAction()
	 * @model required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='loopAction'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	ActionUsage getBodyAction();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.LoopActionUsage#getBodyAction <em>Body Action</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Body Action</em>' reference.
	 * @see #getBodyAction()
	 * @generated
	 */
	void setBodyAction(ActionUsage value);

} // LoopActionUsage

````
