# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/RenderingDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/RenderingDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/RenderingDefinition.java
- source_bytes: 2014
- source_sha256: `7648c8ec390eeb2abb4392e578e3f5b8afcc86e3deaacd50472de3d9830cf8f9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Rendering Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>RenderingDefinition</code> is a <code>PartDefinition</code> that defines a specific rendering of the content of a model view (e.g., symbols, style, layout, etc.).</p>
 * rendering = usages->selectByKind(RenderingUsage)
 * specializesFromLibrary('Views::Rendering')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.RenderingDefinition#getRendering <em>Rendering</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getRenderingDefinition()
 * @model
 * @generated
 */
public interface RenderingDefinition extends PartDefinition {
	/**
	 * Returns the value of the '<em><b>Rendering</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.RenderingUsage}.
	 * <p>
	 * This feature subsets the following features:
	 * </p>
	 * <ul>
	 *   <li>'{@link org.omg.sysml.lang.sysml.Definition#getUsage() <em>Usage</em>}'</li>
	 * </ul>
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>usages</code> of a <code>RenderingDefinition</code> that are <code>RenderingUsages</code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Rendering</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getRenderingDefinition_Rendering()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='featuringRenderingDefinition'"
	 *        annotation="subsets"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<RenderingUsage> getRendering();

} // RenderingDefinition

````
