# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Conjugation.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Conjugation.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Conjugation.kerml
- source_bytes: 107
- source_sha256: `692d4259e957d263495a2196721ef2b6feb1edf77d842ffabbaf6432efeb5e97`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Conjugation {
	class A {
		in feature f;
	}
	
	class B conjugates A;
	
	feature g ~ B::f;
}
````
