# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Import Tests/AliasImport.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Import Tests/AliasImport.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Import Tests/AliasImport.sysml
- source_bytes: 206
- source_sha256: `fd34df8407a75130e25f526b9cae74f9cf87531410ffcdc00d6d9986bc9d1d25`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package AliasImport {
	package Definitions {
	    part def Vehicle;
	    
	    alias Car for Vehicle;
	}
	
	package Usages {
	    private import Definitions::Car;
	
	    part vehicle : Car;
	}
}
````
