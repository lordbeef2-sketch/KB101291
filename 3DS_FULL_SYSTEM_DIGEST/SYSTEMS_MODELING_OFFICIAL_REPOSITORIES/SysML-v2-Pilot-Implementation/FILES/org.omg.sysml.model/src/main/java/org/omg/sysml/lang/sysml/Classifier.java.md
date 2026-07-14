# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Classifier.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Classifier.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Classifier.java
- source_bytes: 2797
- source_sha256: `eeb72db87d39346cb378e6fbfaaa46d514dc01be9662edec9588ba890005abea`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Classifier</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>Classifier</code> is a <code>Type</code> that classifies:</p>
 * 
 * <ul>
 * 	<li>Things (in the universe) regardless of how <code>Features</code> relate them. (These are interpreted semantically as sequences of exactly one thing.)</li>
 * 	<li>How the above things are related by <code>Features.</code> (These are interpreted semantically as sequences of multiple things, such that the last thing in the sequence is also classified by the <code>Classifier</code>. Note that this means that a <code>Classifier</code> modeled as specializing a <code>Feature</code> cannot classify anything.)</li>
 * </ul>
 * 
 * 
 * ownedSubclassification = 
 *     ownedSpecialization->selectByKind(Subclassification)
 * multiplicity <> null implies multiplicity.featuringType->isEmpty()
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Classifier#getOwnedSubclassification <em>Owned Subclassification</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getClassifier()
 * @model
 * @generated
 */
public interface Classifier extends Type {
	/**
	 * Returns the value of the '<em><b>Owned Subclassification</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.Subclassification}.
	 * It is bidirectional and its opposite is '{@link org.omg.sysml.lang.sysml.Subclassification#getOwningClassifier <em>Owning Classifier</em>}'.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Type#getOwnedSpecialization() <em>Owned Specialization</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>ownedSpecializations</code> of this <code>Classifier</code> that are <code>Subclassifications</code>, for which this <code>Classifier</code> is the <code>subclassifier</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Owned Subclassification</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getClassifier_OwnedSubclassification()
	 * @see org.omg.sysml.lang.sysml.Subclassification#getOwningClassifier
	 * @model opposite="owningClassifier" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<Subclassification> getOwnedSubclassification();

} // Classifier

````
