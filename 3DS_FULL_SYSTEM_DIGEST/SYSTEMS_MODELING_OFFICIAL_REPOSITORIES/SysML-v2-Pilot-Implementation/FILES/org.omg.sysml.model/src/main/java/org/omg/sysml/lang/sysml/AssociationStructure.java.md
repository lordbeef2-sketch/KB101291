# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssociationStructure.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssociationStructure.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/AssociationStructure.java
- source_bytes: 1016
- source_sha256: `8062b19f6cab257e63384fa3a18e7c921a3c4c6d601f399a7a67974a4fbfce93`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Association Structure</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>AssociationStructure</code> is an <code>Association</code> that is also a <code>Structure</code>, classifying link objects that are both links and objects. As objects, link objects can be created and destroyed, and their non-end <code>Features</code> can change over time. However, the values of the end <code>Features</code> of a link object are fixed and cannot change over its lifetime.</p>
 * specializesFromLibrary('Objects::LinkObject')
 * endFeature->size() = 2 implies
 *     specializesFromLibrary('Objects::BinaryLinkObject')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getAssociationStructure()
 * @model
 * @generated
 */
public interface AssociationStructure extends Association, Structure {
} // AssociationStructure

````
