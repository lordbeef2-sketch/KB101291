# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/04. Subsetting/Subsetting Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/04. Subsetting/Subsetting Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/04. Subsetting/Subsetting Example.sysml
- source_bytes: 356
- source_sha256: `3bc47e36ff49bef7900652f448400704651423335c66fe22b5e75cce3e192a0e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Subsetting Example' {
	
	part def Vehicle {
		part parts : VehiclePart[*];
		
		part eng : Engine subsets parts;
		part trans : Transmission subsets parts;
		part wheels : Wheel[4] :> parts;
	}
	
	abstract part def VehiclePart;
	part def Engine :> VehiclePart;
	part def Transmission :> VehiclePart;
	part def Wheel :> VehiclePart;
}
````
