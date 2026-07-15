# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/10. Ports/Port Conjugation Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/10. Ports/Port Conjugation Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/10. Ports/Port Conjugation Example.sysml
- source_bytes: 332
- source_sha256: `4049898918adb451a3caf4f110abde37628085cbb668465d7a041fbfcfd7fa5c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Port Conjugation Example' {
	
	attribute def Temp;
	
	part def Fuel;
	
	port def FuelPort {
		attribute temperature : Temp;
		out item fuelSupply : Fuel;
		in item fuelReturn : Fuel;
	}
	
	part def FuelTank {
		port fuelTankPort : FuelPort;
	}
	
	part def Engine {
		port engineFuelPort : ~FuelPort;
	}
}
````
