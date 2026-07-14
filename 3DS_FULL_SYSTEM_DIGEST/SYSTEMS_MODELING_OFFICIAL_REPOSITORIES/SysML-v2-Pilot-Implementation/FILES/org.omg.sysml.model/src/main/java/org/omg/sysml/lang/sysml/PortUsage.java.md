# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortUsage.java
- source_bytes: 2595
- source_sha256: `dc90e53e5cf3d05c58d9c9c734595d07e23561237daee037c345badf528ec2ff`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Port Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>PortUsage</code> is a usage of a <code>PortDefinition</code>. A <code>PortUsage</code> itself as well as all its <code>nestedUsages</code> must be referential (non-composite).</p>
 * nestedUsage->
 *     reject(oclIsKindOf(PortUsage))->
 *     forAll(not isComposite)
 * specializesFromLibrary('Ports::ports')
 * isComposite and owningType <> null and
 * (owningType.oclIsKindOf(PortDefinition) or
 *  owningType.oclIsKindOf(PortUsage)) implies
 *     specializesFromLibrary('Ports::Port::subports')
 * owningType = null or
 * not owningType.oclIsKindOf(PortDefinition) and
 * not owningType.oclIsKindOf(PortUsage) implies
 *     isReference
 * owningType <> null and
 * (owningType.oclIsKindOf(PartDefinition) or
 *  owningType.oclIsKindOf(PartUsage)) implies
 *     specializesFromLibrary('Parts::Part::ownedPorts')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.PortUsage#getPortDefinition <em>Port Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPortUsage()
 * @model
 * @generated
 */
public interface PortUsage extends OccurrenceUsage {
	/**
	 * Returns the value of the '<em><b>Port Definition</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.PortDefinition}.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.OccurrenceUsage#getOccurrenceDefinition() <em>Occurrence Definition</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>occurrenceDefinitions</code> of this <code>PortUsage</code>, which must all be <code>PortDefinitions<code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Port Definition</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPortUsage_PortDefinition()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='definedPort'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<PortDefinition> getPortDefinition();

} // PortUsage

````
