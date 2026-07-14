# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/05. Redefinition/Redefinition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/05. Redefinition/Redefinition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/05. Redefinition/Redefinition Example.sysml
- source_bytes: 455
- source_sha256: `9dcc3eb04eddbb7a94900e0402283398ba449c278af61ad98a10a34bd7e4593a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Redefinition Example' {

	part def Vehicle {
		part eng : Engine;
	}
	part def SmallVehicle :> Vehicle {
		part smallEng : SmallEngine redefines eng;
	}
	part def BigVehicle :> Vehicle {
		part bigEng : BigEngine :>> eng;
	}

	part def Engine {
		part cyl : Cylinder[4..6];
	}
	part def SmallEngine :> Engine {
		part redefines cyl[4];
	}
	part def BigEngine :> Engine {
		part redefines cyl[6];
	}

	part def Cylinder;
}

````
