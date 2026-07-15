# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/PortDefinition.java
- source_bytes: 3206
- source_sha256: `9c4d92cfd30db6f34145792924230ee82a59a08cd555d44b34cb10a2e478e53c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Port Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>PortDefinition</code> defines a point at which external entities can connect to and interact with a system or part of a system. Any <code>ownedUsages</code> of a <code>PortDefinition</code>, other than <code>PortUsages</code>, must not be composite.</p>
 * 
 * 
 * 
 * conjugatedPortDefinition = 
 * let conjugatedPortDefinitions : OrderedSet(ConjugatedPortDefinition) =
 *     ownedMember->selectByKind(ConjugatedPortDefinition) in
 * if conjugatedPortDefinitions->isEmpty() then null
 * else conjugatedPortDefinitions->first()
 * endif
 * ownedUsage->
 *     reject(oclIsKindOf(PortUsage))->
 *     forAll(not isComposite)
 * not oclIsKindOf(ConjugatedPortDefinition) implies
 *     ownedMember->
 *         selectByKind(ConjugatedPortDefinition)->
 *         size() = 1
 * specializesFromLibrary('Ports::Port')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.PortDefinition#getConjugatedPortDefinition <em>Conjugated Port Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPortDefinition()
 * @model
 * @generated
 */
public interface PortDefinition extends OccurrenceDefinition, Structure {
	/**
	 * Returns the value of the '<em><b>Conjugated Port Definition</b></em>' reference.
	 * It is bidirectional and its opposite is '{@link org.omg.sysml.lang.sysml.ConjugatedPortDefinition#getOriginalPortDefinition <em>Original Port Definition</em>}'.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Namespace#getOwnedMember() <em>Owned Member</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>ConjugatedPortDefinition</code> that is conjugate to this <code>PortDefinition</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Conjugated Port Definition</em>' reference.
	 * @see #setConjugatedPortDefinition(ConjugatedPortDefinition)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getPortDefinition_ConjugatedPortDefinition()
	 * @see org.omg.sysml.lang.sysml.ConjugatedPortDefinition#getOriginalPortDefinition
	 * @model opposite="originalPortDefinition" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	ConjugatedPortDefinition getConjugatedPortDefinition();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.PortDefinition#getConjugatedPortDefinition <em>Conjugated Port Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Conjugated Port Definition</em>' reference.
	 * @see #getConjugatedPortDefinition()
	 * @generated
	 */
	void setConjugatedPortDefinition(ConjugatedPortDefinition value);

} // PortDefinition

````
