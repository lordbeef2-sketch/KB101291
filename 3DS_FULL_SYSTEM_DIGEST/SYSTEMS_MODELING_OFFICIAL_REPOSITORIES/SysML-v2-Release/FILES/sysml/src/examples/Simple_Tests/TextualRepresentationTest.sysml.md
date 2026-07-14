# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/TextualRepresentationTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/TextualRepresentationTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/TextualRepresentationTest.sysml
- source_bytes: 396
- source_sha256: `f50c3754f3747867c7590e730020ada778ed74d9827adca49b4f778e85b1cf83`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package TextualRepresentationTest {
	private import ScalarValues::Real;
	
	item def C {
	    attribute x: Real;
	    assert constraint x_constraint {
		    rep inOCL language "ocl" 
		        /* self.x > 0.0 */
	    }
	}
	
	action def setX {
		in c : C;
		in newX : Real;
		
	    language "alf" 
	        /* c.x = newX;
	         * WriteLine("Set new x");
	         */
	}
	
}
````
