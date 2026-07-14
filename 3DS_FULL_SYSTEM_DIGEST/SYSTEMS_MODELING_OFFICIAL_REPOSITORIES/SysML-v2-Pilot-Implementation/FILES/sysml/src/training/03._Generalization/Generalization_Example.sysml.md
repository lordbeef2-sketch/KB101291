# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/03. Generalization/Generalization Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/03. Generalization/Generalization Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/03. Generalization/Generalization Example.sysml
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
