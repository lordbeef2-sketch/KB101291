# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenModelGeneratorAdapterFactory.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenModelGeneratorAdapterFactory.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenModelGeneratorAdapterFactory.java
- source_bytes: 960
- source_sha256: `8db8b85aa98b8c09948aba3b460fcb003b3143d0e56308f68b3b56d2fe1cdfbd`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.uml.ecore.importer;

import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.uml2.codegen.ecore.genmodel.generator.GenModelGeneratorAdapterFactory;

/**
 * SysML-specific UML2 GenModel generator adapter factory.
 *
 * <p>
 * This factory preserves the default UML2 generation behavior and only replaces
 * the {@code GenClass} adapter with a subclass that post-processes generated
 * implementation classes to use the local SysML helper-list utilities.
 * </p>
 */
public class SysMLGenModelGeneratorAdapterFactory extends GenModelGeneratorAdapterFactory {

	/**
	 * Returns a singleton {@link SysMLGenClassGeneratorAdapter}.
	 *
	 * @return the SysML-aware GenClass generator adapter
	 */
	@Override
	public Adapter createGenClassAdapter() {
		if (genClassGeneratorAdapter == null) {
			genClassGeneratorAdapter = new SysMLGenClassGeneratorAdapter(this);
		}
		return genClassGeneratorAdapter;
	}
}

````
