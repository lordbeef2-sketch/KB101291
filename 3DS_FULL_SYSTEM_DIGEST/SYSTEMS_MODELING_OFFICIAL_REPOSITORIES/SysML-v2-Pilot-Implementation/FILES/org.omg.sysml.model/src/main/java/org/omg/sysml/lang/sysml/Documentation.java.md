# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Documentation.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Documentation.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Documentation.java
- source_bytes: 2520
- source_sha256: `639223b595805aeba3d5499f1e0025a3337785edbff14e92b17dc650ef9a0abf`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Documentation</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p><code>Documentation</code> is a <code>Comment</code> that specifically documents a <code>documentedElement</code>, which must be its <code>owner</code>.</p>
 * 
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.Documentation#getDocumentedElement <em>Documented Element</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDocumentation()
 * @model
 * @generated
 */
public interface Documentation extends Comment {
	/**
	 * Returns the value of the '<em><b>Documented Element</b></em>' reference.
	 * It is bidirectional and its opposite is '{@link org.omg.sysml.lang.sysml.Element#getDocumentation <em>Documentation</em>}'.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Element#getOwner() <em>Owner</em>}'</li>
	 * </ul>
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.AnnotatingElement#getAnnotatedElement() <em>Annotated Element</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>Element</code> that is documented by this <code>Documentation</code>.</p>
	 * 
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Documented Element</em>' reference.
	 * @see #setDocumentedElement(Element)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDocumentation_DocumentedElement()
	 * @see org.omg.sysml.lang.sysml.Element#getDocumentation
	 * @model opposite="documentation" required="true" transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="redefines"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Element getDocumentedElement();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.Documentation#getDocumentedElement <em>Documented Element</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Documented Element</em>' reference.
	 * @see #getDocumentedElement()
	 * @generated
	 */
	void setDocumentedElement(Element value);

} // Documentation

````
