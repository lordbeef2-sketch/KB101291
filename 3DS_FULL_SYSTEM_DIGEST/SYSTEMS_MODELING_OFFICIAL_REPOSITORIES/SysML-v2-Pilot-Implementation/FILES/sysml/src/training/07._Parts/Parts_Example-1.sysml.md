# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/07. Parts/Parts Example-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/07. Parts/Parts Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/07. Parts/Parts Example-1.sysml
- source_bytes: 387
- source_sha256: `309715afa83e60c5f282e34bd8b3dccf8a54d7a4a42649ea208773e2438a0b4c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Parts Example-1' {
	
	// Definitions
	
	part def Vehicle {
		part eng : Engine;
	}
	
	part def Engine {
		part cyl : Cylinder[4..6];
	}
	
	part def Cylinder;
	
	// Usages
	
	part smallVehicle : Vehicle {
		part redefines eng {
			part redefines cyl[4];
		}
	}
	
	part bigVehicle : Vehicle {
		part redefines eng {
			part redefines cyl[6];
		}
	}
	
}
````
