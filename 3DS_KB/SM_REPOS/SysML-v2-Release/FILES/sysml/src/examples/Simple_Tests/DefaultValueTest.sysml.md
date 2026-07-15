# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/DefaultValueTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/DefaultValueTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/DefaultValueTest.sysml
- source_bytes: 235
- source_sha256: `b770da8931607bd2a7c0c631fd7f4e004efe3afa1beae7951e6ded5bb4a0c61f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package DefaultValueTest {
	
	part def V {
		attribute m default = 10;
		attribute n = 20;
	}
	
	part v1 : V {
		attribute :>> m = 20;
	}
	
	part def W :> V {
		attribute :>> m default = n;
	}
	
	part v2 = new W();
	
}
````
