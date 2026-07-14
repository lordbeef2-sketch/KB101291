# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/ParameterTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/ParameterTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/ParameterTest.sysml
- source_bytes: 355
- source_sha256: `e9f7e8a9f5b486f1b2a03391d2d0b379ccbf7fe32ab4786b434d8e9966437c12`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ParameterTest {
	attribute def A {
		attribute x : ScalarValues::String;
		attribute y : A;
	}
	
	attribute a : A;
	
	calc def F { in p : A; in q : ScalarValues::Integer; return :  ScalarValues::Integer; }
	
	attribute f = F(a, 2);
	attribute g = F(q = 1, p = a);
	
	attribute b = new A(y=a, x=""); 
	attribute c = new A("test2");
}
````
