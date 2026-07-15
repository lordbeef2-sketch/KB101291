# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/TextualRepresentation.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/TextualRepresentation.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/TextualRepresentation.kerml
- source_bytes: 361
- source_sha256: `064456e4d6d453e04d828390ae8d886af4f36dc01eda0ed5b482f8a5be1cc1f9`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package TextualRepresentation {
	private import ScalarValues::Real;
	
	class C {
	    feature x: Real;
	    inv x_constraint {
		    rep inOCL language "ocl" 
		        /* self.x > 0.0 */
	    }
	}
	
	behavior setX { in c : C; in newX : Real;
	    language "alf" 
	        /* c.x = newX;
	         * WriteLine("Set new x");
	         */
	}
	
}
````
