# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/08. Items/Items Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/08. Items/Items Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/08. Items/Items Example.sysml
- source_bytes: 240
- source_sha256: `5eb1376cadf723de29fd97556d00faa11504b1adfaa4a622bd229eb815edf468`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Items Example' {
	private import ScalarValues::*;
	
	item def Fuel;
	item def Person;
	
	part def Vehicle {
		attribute mass : Real;
		
		ref item driver : Person;

		part fuelTank {
			item fuel: Fuel;
		}		
	}
	
}
````
