# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/03. Generalization/Generalization Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/03. Generalization/Generalization Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/03. Generalization/Generalization Example.sysml
- source_bytes: 352
- source_sha256: `8ff8fe67838af859af06b8d1e54f724dbe7d1ffde65ba1f88b5d73d0be10740d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Generalization Example' {

	abstract part def Vehicle;
	
	part def HumanDrivenVehicle specializes Vehicle {
		ref part driver : Person;
	}
	
	part def PoweredVehicle :> Vehicle {
		part eng : Engine;
	}
	
	part def HumanDrivenPoweredVehicle :> 
		HumanDrivenVehicle, PoweredVehicle;
	
	part def Engine;	
	part def Person;
	
}
````
