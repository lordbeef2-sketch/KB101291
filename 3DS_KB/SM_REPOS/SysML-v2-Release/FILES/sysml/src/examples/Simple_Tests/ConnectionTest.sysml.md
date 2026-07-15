# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/ConnectionTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/ConnectionTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/ConnectionTest.sysml
- source_bytes: 991
- source_sha256: `81dea0d21c6ea696da006f2cae5f4851d7ba66cad050aab81de428cd72ac5a64`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ConnectionTest {
	
	part p {
		part x {
			part x1;
		}
	}
	
	part def P {
		part y;

		connect p to y;
		
		part p1 :> p;
	
		connect p1.x to y;
		connect p1.x.x1 to y;
		
		part a;
		part b;
		
		bind a = b;
		binding ab bind a = b;
		binding ab1 : AB bind a = b;
		
		first a then b;
		succession s first a then b;
		succession s1 : AB first a then b;
	}

	abstract connection def C {
		part p;
		end end1;
		end end2;
		end end3;
	}
	
	part d1;
	part d2;
	part d3;
	part d4;
	
	connection bus : C connect (d1, d2, d3, d4);
	
	connection : C {
	    end :>> end1 ::> d1;
	    end end2 ::> d2;
	    end end3 ::> d3;
	}
	
	connection {
		part q;
		end ref end1 ::> d1 :> q;
		end end2 ::> d2;
	}
	
	abstract flow def F;
	
	message : F from p to p;
	
	part def A {
	    ref b : B;
	}
	
	part def B;
	
	connection def AB {
	    end [1] item a : A {
	    	@M;
	    }
	    end b : B;
	}
	
	metadata def M;
	
	
}
````
