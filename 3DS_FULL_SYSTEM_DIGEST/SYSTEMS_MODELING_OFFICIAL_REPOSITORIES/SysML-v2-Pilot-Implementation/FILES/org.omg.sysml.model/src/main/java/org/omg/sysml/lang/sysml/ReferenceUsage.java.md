# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReferenceUsage.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReferenceUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/ReferenceUsage.java
- source_bytes: 974
- source_sha256: `b4dc13d857cfb11143c18843187f0d544e7caa56f6182f7b8555bb47fef24db5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;


/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Reference Usage</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>ReferenceUsage</code> is a <code>Usage</code> that specifies a non-compositional (<code>isComposite = false</code>) reference to something. The <code>definition</code> of a <code>ReferenceUsage</code> can be any kind of <code>Classifier</code>, with the default being the top-level <code>Classifier</code> <code><em>Base::Anything</em></code> from the Kernel Semantic Library. This allows the specification of a generic reference without distinguishing if the thing referenced is an attribute value, item, action, etc.</p>
 * isReference
 * <!-- end-model-doc -->
 *
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getReferenceUsage()
 * @model
 * @generated
 */
public interface ReferenceUsage extends Usage {
} // ReferenceUsage

````
