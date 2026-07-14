# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Geometry Examples/CarWithEnvelopingShape.sysml
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
