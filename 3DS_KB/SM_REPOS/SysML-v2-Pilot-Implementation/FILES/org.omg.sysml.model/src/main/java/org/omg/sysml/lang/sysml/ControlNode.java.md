# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ControlNode.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ControlNode.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ControlNode.java
- source_bytes: 2338
- source_sha256: `3ab6f517730d8562b1a4989c093645c9337b9ac6dc14ee18e7960d43b1316f41`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Control Node</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ControlNode</code> is an <code>ActionUsage</code> that does not have any inherent behavior but provides constraints on incoming and outgoing <code>Successions</code> that are used to control other <code>Actions</code>. A <code>ControlNode</code> must be a composite owned <code>usage</code> of an <code>ActionDefinition</code> or <code>ActionUsage</code>.</p>
 * 
 * sourceConnector->selectByKind(Succession)->
 *     collect(connectorEnd->at(1).multiplicity)->
 *     forAll(sourceMult | 
 *         multiplicityHasBounds(sourceMult, 1, 1))
 * owningType <> null and 
 * (owningType.oclIsKindOf(ActionDefinition) or
 *  owningType.oclIsKindOf(ActionUsage))
 * targetConnector->selectByKind(Succession)->
 *     collect(connectorEnd->at(2).multiplicity)->
 *     forAll(targetMult | 
 *         multiplicityHasBounds(targetMult, 1, 1))
 * specializesFromLibrary('Action::Action::controls')
 * isComposite
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getControlNode()
 * @model abstract="true"
 * @generated
 */
public interface ControlNode extends ActionUsage {
	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>Check that the given <code>Multiplicity</code> has <code>lowerBound</code> and <code>upperBound</code> expressions that are model-level evaluable to the given <code>lower</code> and <code>upper</code> values.</p>
	 * mult <> null and
	 * if mult.oclIsKindOf(MultiplicityRange) then
	 *     mult.oclAsType(MultiplicityRange).hasBounds(lower, upper)
	 * else
	 *     mult.allSuperTypes()->exists(
	 *         oclisKindOf(MultiplicityRange) and
	 *         oclAsType(MultiplicityRange).hasBounds(lower, upper)
	 * endif
	 * <!-- end-model-doc -->
	 * @model required="true" ordered="false" multRequired="true" multOrdered="false" lowerRequired="true" lowerOrdered="false" upperRequired="true" upperOrdered="false"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	boolean multiplicityHasBounds(Multiplicity mult, int lower, int upper);

} // ControlNode

````
