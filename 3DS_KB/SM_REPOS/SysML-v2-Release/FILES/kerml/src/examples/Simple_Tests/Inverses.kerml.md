# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Inverses.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Inverses.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Inverses.kerml
- source_bytes: 263
- source_sha256: `6ab43c8e7062cfa48a2f0f9ed54b73356098244874ac64c4c89d34f5e43101cd`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Inverses {
	class A {
		feature f : B inverse of B::g disjoint from h;
		feature h : B;
	}
	
	class B {
		feature g : A;
	}
	
	inverse B::g of A::f;
	inverting Invert inverse B::g.f of A::h;
	
	feature gg : A featured by B inverse of A::f;
}
````
