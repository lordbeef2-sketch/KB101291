# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/12-Dependency Relationships/12a-Dependency.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/12-Dependency Relationships/12a-Dependency.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/12-Dependency Relationships/12a-Dependency.sysml
- source_bytes: 308
- source_sha256: `18115107485f37a0093d3ebe506beb57c5467edbfa8b93cf3625330c04e7480c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '12a-Dependency' {
	
	package 'Application Layer';
	package 'Service Layer';
	package 'Data Layer';
	
	dependency Use from 'Application Layer' to 'Service Layer';
	dependency from 'Service Layer' to 'Data Layer';
	
	attribute x;
	attribute y;
	attribute z;
	
	dependency z to x, y;
	
}
````
