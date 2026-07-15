# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/UseCaseDefinition.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/UseCaseDefinition.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/UseCaseDefinition.java
- source_bytes: 2114
- source_sha256: `f36d935c1210faadea79e0ca5364e8840f9756bcf7442b5f513fab6458b4cb8b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 */
package org.omg.sysml.lang.sysml;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Use Case Definition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <!-- begin-model-doc -->
 * <p>A <code>UseCaseDefinition</code> is a <code>CaseDefinition</code> that specifies a set of actions performed by its subject, in interaction with one or more actors external to the subject. The objective is to yield an observable result that is of value to one or more of the actors.</p>
 * 
 * includedUseCase = ownedUseCase->
 *     selectByKind(IncludeUseCaseUsage).
 *     useCaseIncluded
 * specializesFromLibrary('UseCases::UseCase')
 * <!-- end-model-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link org.omg.sysml.lang.sysml.UseCaseDefinition#getIncludedUseCase <em>Included Use Case</em>}</li>
 * </ul>
 *
 * @see org.omg.sysml.lang.sysml.SysMLPackage#getUseCaseDefinition()
 * @model
 * @generated
 */
public interface UseCaseDefinition extends CaseDefinition {
	/**
	 * Returns the value of the '<em><b>Included Use Case</b></em>' reference list.
	 * The list contents are of type {@link org.omg.sysml.lang.sysml.UseCaseUsage}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * <!-- begin-model-doc -->
	 * <p>The <code>UseCaseUsages</code> that are included by this <code>UseCaseDefinition</code>, which are the <code>useCaseIncludeds</code> of the <code>IncludeUseCaseUsages</code> owned by this <code>UseCaseDefinition<code>.</p>
	 * <!-- end-model-doc -->
	 * @return the value of the '<em>Included Use Case</em>' reference list.
	 * @see org.omg.sysml.lang.sysml.SysMLPackage#getUseCaseDefinition_IncludedUseCase()
	 * @model transient="true" volatile="true" derived="true"
	 *        annotation="http://schema.omg.org/spec/MOF/2.0/emof.xml#Property.oppositeRoleName body='includingUseCaseDefinition'"
	 *        annotation="http://www.omg.org/spec/SysML"
	 * @generated
	 */
	EList<UseCaseUsage> getIncludedUseCase();

} // UseCaseDefinition

````
