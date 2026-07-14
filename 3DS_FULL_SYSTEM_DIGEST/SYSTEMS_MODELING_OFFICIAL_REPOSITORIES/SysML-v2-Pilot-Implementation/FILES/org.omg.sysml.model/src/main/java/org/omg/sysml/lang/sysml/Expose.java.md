# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Expose.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Expose.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Expose.java
- source_bytes: 790
- source_sha256: `3623b62b995bf643591c7388fb0778ebca18a16f3c5ccad0e0ead87d701e7b47`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Expose</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>Expose</code> is an <code>Import</code> of <code>Memberships</code> into a <code>ViewUsage</code> that provide the <code>Elements</code> to be included in a view. Visibility is always ignored for an <code>Expose</code> (i.e., <code>isImportAll = true</code>).</p>
 * isImportAll
 * importOwningNamespace.oclIsType(ViewUsage)
 * visibility = VisibilityKind::protected
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getExpose()
 * @model abstract="true"
 * @generated
 */
public interface Expose extends Import {
} // Expose

````
