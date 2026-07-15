# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/TextualRepresentation.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/TextualRepresentation.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/TextualRepresentation.kerml
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
