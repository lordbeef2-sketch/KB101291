# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/ArgumentResolution.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/ArgumentResolution.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/ArgumentResolution.kerml
- source_bytes: 223
- source_sha256: `ef41aea0c874d82dd385268eb17c632749ad5b941155cd7b2a5ce01fc6be35a2`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package ArgumentResolutionBug {
	class A {
		feature x;
	}
	
	behavior B  {
		in feature x;
		out feature : A = new A(x);
	}
	
	class C {
		feature a : A;
		feature b : B;
		
		connector a ::> a.x to b;
	}
}
````
