# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/02. Part Definitions/Part Definition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/02. Part Definitions/Part Definition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/02. Part Definitions/Part Definition Example.sysml
- source_bytes: 380
- source_sha256: `2340cd33421a34ec41bdc0db4b26375fc673c181373112d1f658bc1011df64d9`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Part Definition Example' {
	private import ScalarValues::*;
	
	part def Vehicle {
		attribute mass : Real;
		attribute status : VehicleStatus;
		
		part eng : Engine;
		
		ref part driver : Person;
	}
	
	attribute def VehicleStatus {
		attribute gearSetting : Integer;
		attribute acceleratorPosition : Real;
	}
	
	part def Engine;	
	part def Person;
}
````
