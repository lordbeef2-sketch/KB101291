# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/KerML Spec Annex A Examples/A-2-Atoms.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/KerML Spec Annex A Examples/A-2-Atoms.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/KerML Spec Annex A Examples/A-2-Atoms.kerml
- source_bytes: 356
- source_sha256: `9d972fecbc110cc1af256955add63a3f7d9875c99b4201faaa5ab2e635efc544`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Atoms {
	doc
	/* This package defines a keyword (atom) for classifiers with
	 * exactly one instance and are disjoint from any others
	 * marked with this keyword.
	 */

	private import Metaobjects::Metaobject;
	
	classifier Atom;
	metaclass <atom> AtomMetadata specializes Metaobject {
		baseType = Atom meta KerML::Classifier;
	}
}

````
