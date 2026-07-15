# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/37. Dependencies/Dependency Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/37. Dependencies/Dependency Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/37. Dependencies/Dependency Example.sysml
- source_bytes: 514
- source_sha256: `9e0bc2a461abbb4eeaa09356725a3169361a7c3f7673b566d23d01e444ce6e04`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Dependency Example' {
	
	part 'System Assembly' {
		part 'Computer Subsystem' {
			// ...
		}
		
		part 'Storage Subsystem' {
			// ...
		}
	}
	
	package 'Software Design' {
		item def MessageSchema {
			// ...
		}
		item def DataSchema {
			// ...
		}
	}
	
	dependency from 'System Assembly'::'Computer Subsystem' to 'Software Design';
	
	dependency Schemata 
		from 'System Assembly'::'Storage Subsystem' 
		to 'Software Design'::MessageSchema, 'Software Design'::DataSchema;
}
````
