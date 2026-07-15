# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MetadataUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MetadataUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/MetadataUsage.java
- source_bytes: 2685
- source_sha256: `610fd334711bf3b9ffa04255fb159c933e8e46c0a6ed8b927dd65a03850b439b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Metadata Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A  <code>MetadataUsage</code> is a <code>Usage</code> and a <code>MetadataFeature</code>, used to annotate other <code>Elements</code> in a system model with metadata. As a <code>MetadataFeature</code>, its type must be a <code>Metaclass</code>, which will nominally be a <code>MetadataDefinition</code>. However, any kernel <code>Metaclass</code> is also allowed, to permit use of <code>Metaclasses</code> from the Kernel Model Libraries.</p>
 * specializesFromLibrary('Metadata::metadataItems')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.MetadataUsage#getMetadataDefinition <em>Metadata Definition</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getMetadataUsage()
 * @model
 * @generated
 */
public interface MetadataUsage extends ItemUsage, MetadataFeature {
	/**
	 * Returns the value of the '<em><b>Metadata Definition</b></em>' reference.
	 * <p>
	 * This feature redefines the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.ItemUsage#getItemDefinition() <em>Item Definition</em>}'</li>
	 *   <li>'{@link org.omg.sysml.lang.sysml.MetadataFeature#getMetaclass() <em>Metaclass</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>MetadataDefinition</code> that is the <code>definition</code> of this <code>MetadataUsage</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Metadata Definition</em>' reference.
	 * @see #setMetadataDefinition(Metaclass)
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getMetadataUsage_MetadataDefinition()
	 * @model transient="true" volatile="true" derived="true" ordered="false"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='definedMetadata'"
	 *        annotation="redefines"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	Metaclass getMetadataDefinition();

	/**
	 * Sets the value of the '{@link org.omg.sysml.lang.sysml.MetadataUsage#getMetadataDefinition <em>Metadata Definition</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Metadata Definition</em>' reference.
	 * @see #getMetadataDefinition()
	 * @generated
	 */
	void setMetadataDefinition(Metaclass value);

} // MetadataUsage

````
