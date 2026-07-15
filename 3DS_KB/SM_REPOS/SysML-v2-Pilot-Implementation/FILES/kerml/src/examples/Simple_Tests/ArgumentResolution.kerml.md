# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/ArgumentResolution.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/ArgumentResolution.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/ArgumentResolution.kerml
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
