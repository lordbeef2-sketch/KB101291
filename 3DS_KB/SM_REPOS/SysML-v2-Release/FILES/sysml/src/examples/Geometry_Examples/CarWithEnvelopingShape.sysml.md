# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml
- source_bytes: 346
- source_sha256: `6b5156d073d31d52b95748419c4b5836805ea6143ae33509f414bdfe2d937b3a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package CarWithEnvelopingShape {
	private import ShapeItems::Box;
	private import SI::mm;

	part def Car {
		doc
		/*
		 * Example car with simple enveloping shape that is a solid box
		 */
	
		item boundingBox : Box [1] :> boundingShapes {
			:>> length = 4800 [mm];
			:>> width  = 1840 [mm];
			:>> height = 1350 [mm];
		}
	}
}
````
