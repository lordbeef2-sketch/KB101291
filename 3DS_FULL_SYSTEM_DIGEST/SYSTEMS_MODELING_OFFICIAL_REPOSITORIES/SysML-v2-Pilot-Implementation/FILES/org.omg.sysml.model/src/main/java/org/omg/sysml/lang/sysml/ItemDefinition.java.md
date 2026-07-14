# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ItemDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ItemDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ItemDefinition.java
- source_bytes: 905
- source_sha256: `388e9a9fbd4aa6515fe89fcb98669ad05021484dc1c25d926ad45e2111936e11`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Item Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>An <code>ItemDefinition</code> is an <code>OccurrenceDefinition</code> of the <code>Structure</code> of things that may themselves be systems or parts of systems, but may also be things that are acted on by a system or parts of a system, but which do not necessarily perform actions themselves. This includes items that can be exchanged between parts of a system, such as water or electrical signals.</p>
 * 
 * specializesFromLibrary('Items::Item')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getItemDefinition()
 * @model
 * @generated
 */
public interface ItemDefinition extends OccurrenceDefinition, Structure {
} // ItemDefinition

````
