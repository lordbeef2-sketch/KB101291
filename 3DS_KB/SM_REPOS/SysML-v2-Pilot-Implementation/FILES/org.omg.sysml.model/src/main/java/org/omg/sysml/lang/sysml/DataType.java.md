# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DataType.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DataType.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/DataType.java
- source_bytes: 1156
- source_sha256: `ebd65f5853dc09f717d746fecd2a6c6d148c9077d9f5063001e3333f75b33e76`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Data Type</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>DataType</code> is a <code>Classifier</code> of things (in the universe) that can only be distinguished by how they are related to other things (via Features). This means multiple things classified by the same <code>DataType</code></p>
 * 
 * <ul>
 * 	<li>Cannot be distinguished when they are related to other things in exactly the same way, even when they are intended to be about different things.</li>
 * 	<li>Can be distinguished when they are related to other things in different ways, even when they are intended to be about the same thing.</li>
 * </ul>
 * 
 * ownedSpecialization.general->
 *     forAll(not oclIsKindOf(Class) and 
 *            not oclIsKindOf(Association))
 * specializesFromLibrary('Base::DataValue')
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getDataType()
 * @model
 * @generated
 */
public interface DataType extends Classifier {
} // DataType

````
