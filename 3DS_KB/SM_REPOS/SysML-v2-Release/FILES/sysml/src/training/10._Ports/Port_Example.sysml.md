# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/10. Ports/Port Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/10. Ports/Port Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/10. Ports/Port Example.sysml
- source_bytes: 460
- source_sha256: `15a584ec873eb174f51d7131cbd70cc860c87b70cf60aa7561eae94d95d1658a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Port Example' {
	
	attribute def Temp;
	
	part def Fuel;
	
	port def FuelOutPort {
		attribute temperature : Temp;
		out item fuelSupply : Fuel;
		in item fuelReturn : Fuel;
	}
	
	port def FuelInPort {
		attribute temperature : Temp;
		in item fuelSupply : Fuel;
		out item fuelReturn : Fuel;
	}
	
	part def FuelTankAssembly {
		port fuelTankPort : FuelOutPort;
	}
	
	part def Engine {
		port engineFuelPort : FuelInPort;
	}
}
````
