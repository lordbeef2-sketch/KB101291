# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/10. Ports/Port Conjugation Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/10. Ports/Port Conjugation Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/10. Ports/Port Conjugation Example.sysml
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
