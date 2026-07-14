# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/FeaturePathTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/FeaturePathTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/FeaturePathTest.sysml
- source_bytes: 536
- source_sha256: `ea0eae80b7b1dfd8f2c713b64ef3d3f68de42e1bdc54958394fa1d9463ee8ae3`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package Q {
  part def F {
  	part a : A;
  }
  
  part f : F;
  
  part def A {
    part g = f.a;
  }
  
  part def B {
  	part f : F;
  	part a : A;
  }
  
  part def C {
	part b : B {
	  connect f.a to a.g;
	  bind f.a = a.g;
	}
  
	part c subsets b.f {
	  	part aa subsets a;
	}
	
	flow b.f.a to c.aa;
  }
  
  part e1 {
  	attribute x : E;
  	// Ensure that "e1" resolves correctly.
  	bind e1.x = E::e2;
  }
  
  enum def E {
  	enum e1;
  	enum e2;
  }
  
  part g = new A().g.g.g;
	
}

````
