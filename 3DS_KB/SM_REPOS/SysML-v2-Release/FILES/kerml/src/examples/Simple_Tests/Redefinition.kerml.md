# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Redefinition.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Redefinition.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Redefinition.kerml
- source_bytes: 347
- source_sha256: `e5f74efd661737a4564f9badc715d402d155995dd23a233a26602a6ec86f290c`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Redefinition {
	
	classifier A {
	    feature f;
	}
	
	classifier B specializes A {
	    feature redefines f {
	        feature g;
	    }
	}
	
	classifier C specializes A, B {
	    feature subsets f {
	        feature redefines g;
	    }
	}

	class X {
		feature redefines startShot;
		feature redefines endShot;
	}
}
````
