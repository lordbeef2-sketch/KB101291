# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Geometry Examples/ExternalShapeRefExample.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Geometry Examples/ExternalShapeRefExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Geometry Examples/ExternalShapeRefExample.sysml
- source_bytes: 714
- source_sha256: `57ab77382fed5e508a6a2f13aadb3ce714428826338fff78e3e3074053977c42`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ExternalShapeRefExample {
	private import ScalarValues::String;
	private import ShapeItems::*;
	private import ISQ::mass;
	private import SI::mm;

	metadata def ExternalShapeRef {
		doc
		/*
		 * Metadata to reference an externally defined shape.
		 */
	
		attribute purpose : String[1];
		attribute shapeIri : String[1];
	}
	
	part myBatteryUnit {
	    item :>> shape : Shell {
			metadata ExternalShapeRef {
				purpose = "highLoD";
				shapeIri = "file:/detailed-geometry/LEMS-250W_BatteryHousing_Example.step";
			}
		}		

		private item envelopingBoxBatteryUnit : Box :> envelopingShapes {
			:>> length = 140[mm];
			:>> width = 148[mm];
			:>> height = 90[mm];
		}
	}
}
````
