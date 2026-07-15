# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Inheritance.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Inheritance.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Inheritance.kerml
- source_bytes: 256
- source_sha256: `76c818ba239c56269f93565a697a4edc504c1f0e78415fb0f231bcad38b6233c`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Inheritance {
	class A {
		feature f;
	}
	
	class B specializes A {
		
	}
		
	feature y: A {
		alias x for B::f;
		feature g redefines f;
	}
	
	alias z for y::g;
	
	feature w subsets y;
	
	alias us for w::g;
	
	feature yy: y;
}
````
