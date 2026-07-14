# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/ConjugationTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/ConjugationTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/ConjugationTest.sysml
- source_bytes: 468
- source_sha256: `91deacf8ad3dd3abff60a5c0ac665e46ad2331f48089c0d8b767bf6b88780267`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ConjugationTest {
	port def P;
	
	part def B {
		port p1: P;
		port p2: ~P;
	}
	
	connection def A {
		end port p1: P;
		end port p2: ~P;
	}
	
	interface def I {
		end p1: P;
		end p2: ~P;
	}
	
	part def B1 {
		part p {
			port p1: P;
			port p2: ~P;		
		}
	
		connection a: A {
			end port p3: P ::> p.p1;
			end port p4: ~P ::> p.p2;
		}
		interface i: I {
			end port p3: P ::> p.p1;
			end port p4: ~P ::> p.p2;
		}
	}
	
}
````
