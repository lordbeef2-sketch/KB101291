# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenClassGeneratorAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenClassGeneratorAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/SysMLGenClassGeneratorAdapter.java
- source_bytes: 2056
- source_sha256: `6d87f9261377ad52f3c75ec2c3f90f7186da06225cf189b5c4f1e5ada8877836`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.uml.ecore.importer;

import org.eclipse.emf.codegen.ecore.generator.GeneratorAdapterFactory;
import org.eclipse.emf.codegen.ecore.genmodel.GenClass;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.uml2.codegen.ecore.genmodel.generator.UML2GenClassGeneratorAdapter;

/**
 * GenClass generator adapter that preserves the default UML2 generation logic
 * and normalizes the generated Java class afterwards.
 */
public class SysMLGenClassGeneratorAdapter extends UML2GenClassGeneratorAdapter {

	private final SysMLGeneratedClassNormalizer generatedClassNormalizer;

	/**
	 * Creates the adapter.
	 *
	 * @param generatorAdapterFactory the owning generator adapter factory
	 */
	public SysMLGenClassGeneratorAdapter(GeneratorAdapterFactory generatorAdapterFactory) {
		this(generatorAdapterFactory, new SysMLGeneratedClassNormalizer());
	}

	/**
	 * Creates the adapter with the normalizer used to post-process generated
	 * implementation classes.
	 *
	 * @param generatorAdapterFactory the owning generator adapter factory
	 * @param generatedClassNormalizer the generated source normalizer
	 */
	private SysMLGenClassGeneratorAdapter(
			GeneratorAdapterFactory generatorAdapterFactory,
			SysMLGeneratedClassNormalizer generatedClassNormalizer) {
		super(generatorAdapterFactory);
		this.generatedClassNormalizer = generatedClassNormalizer;
	}

	/**
	 * Normalizes the generated implementation source after the standard class
	 * generation has completed.
	 *
	 * @param object the generated model element
	 * @param projectType the EMF generation project type
	 * @return the diagnostic produced by the superclass post-processing
	 */
	@Override
	protected Diagnostic doPostGenerate(Object object, Object projectType) {
		Diagnostic diagnostic = super.doPostGenerate(object, projectType);
		if (object instanceof GenClass genClass && MODEL_PROJECT_TYPE.equals(projectType)) {
			this.generatedClassNormalizer.normalize(genClass);
		}
		return diagnostic;
	}
}

````
