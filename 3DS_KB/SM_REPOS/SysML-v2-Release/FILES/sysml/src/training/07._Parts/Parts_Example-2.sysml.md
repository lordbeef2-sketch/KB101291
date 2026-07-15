# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/07. Parts/Parts Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/07. Parts/Parts Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/07. Parts/Parts Example-2.sysml
- source_bytes: 416
- source_sha256: `f3cd762f65d6d51e970cac2fd597d0785949a3566066fe8b7d6c9679a9d8e491`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Parts Example-2' {
	
	// Definitions
	
	part def Vehicle;	
	part def Engine;	
	part def Cylinder;
	
	// Usages
	
	part vehicle : Vehicle {
		part eng : Engine {
			part cyl : Cylinder[4..6];
		}
	}
	
	part smallVehicle :> vehicle {
		part redefines eng {
			part redefines cyl[4];
		}
	}
	
	part bigVehicle :> vehicle {
		part redefines eng {
			part redefines cyl[6];
		}
	}
	
}
````
