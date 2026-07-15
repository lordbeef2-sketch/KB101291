# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Types.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Types.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Types.kerml
- source_bytes: 999
- source_sha256: `842b5b8053eb80142e8e90e58d7cd5ac5df9dc1c3699ab7dff4e79f6c69198a7`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Types {
	abstract type A specializes Base::Anything;
	type all x specializes A, Base::things;
	
	// This Type has exactly one instance.
	type Singleton[1] specializes Base::Anything;
	
	type Super specializes Base::Anything {
	    private package P {
	        type Sub specializes Super;
	    }
	    protected feature f : P::Sub;
	}
	
	type B :> Base::Anything;
	
	specialization Gen subtype A specializes B;
	specialization subtype x :> Base::things;
	
	type Original specializes Base::Anything {
	    in feature Input; 
	}
	type Conjugate1 specializes Base::Anything;
	type Conjugate2 specializes Base::Anything;
	conjugation c1 conjugate Conjugate1 conjugates Original; 
	conjugation c2 conjugate Conjugate2 ~ Original; 
	
	type Conjugate3 conjugates Original;
	type Conjugate4 ~ Conjugate1;
	
	type C :> B disjoint from A;
	
	type D :> Base::Anything unions A, B;
	type E :> Base::Anything intersects A, B;
	type F :> Base::Anything differences A, B;
}
````
