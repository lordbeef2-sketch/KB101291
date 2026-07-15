# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/StructuredControlTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/StructuredControlTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/StructuredControlTest.sysml
- source_bytes: 567
- source_sha256: `6859079dc29b625b396679d76f491c942dbc480d3b2700b875cd35bde725fdc7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package StructuredControlTest {
	
	action {
		attribute i : ScalarValues::Integer := 0;
		attribute b : ScalarValues::Boolean;
		
		if i < 0 {
			assign i := 0;
		} else if i == 0 {
			assign i := 1;
		} else {
			assign i := i + 1;
		}
		
		if i > 0 {
			assign i := i + 1;
		}
		
		then action aLoop
		while i > 0 {
			assign i := i - 1;
		} until b;
		
		then while i > 0 {
			assign i := i - 1;
		}
		
		loop {
			assign i := i - 1;
		} until b;
				
		for n : ScalarValues::Integer in (1, 2, 3) {
			assign i := i * n;
		}
	}
}
````
