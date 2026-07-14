# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Structure.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Structure.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/Structure.java
- source_bytes: 832
- source_sha256: `1920ca23784a6aa96b3f2b306b773917e72f37a1e99696c2e032c184727ee9f9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Structure</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>Structure</code> is a <code>Class</code> of objects in the modeled universe that are primarily structural in nature. While such an object is not itself behavioral, it may be involved in and acted on by <code>Behaviors</code>, and it may be the performer of some of them.</p>
 * 
 * specializesFromLibrary('Objects::Object')
 * ownedSpecialization.general->forAll(not oclIsKindOf(Behavior))
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getStructure()
 * @model
 * @generated
 */
public interface Structure extends org.omg.sysml.lang.sysml.Class {
} // Structure

````
