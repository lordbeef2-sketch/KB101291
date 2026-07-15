# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Imports.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Imports.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Imports.kerml
- source_bytes: 525
- source_sha256: `fdcdc033ac07b4477d3aa00082f2bb77138bf40b533800cc68536c2f4174072e`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Imports {

	package P {
		class A;
		class B;
		class C;
	}
	
	package Q {
		class A;
		class D {
			class E;
		}
		package Q1 {
			class D;
			class E;
			private package Q1a {
				class G;
			}
		}
		package Q2 {
			class F;
		}
	}
	
	package R {
		public import Q::*;
	}

	
	package S {
		public import P::*;
		public import Q::**;
		
		class X :> A;
		class Y :> D;
		class Z :> F;
	}
	
	package S1 {
		public import P::*;
		public import R::*;
		
		class X :> A;
	}
}
````
