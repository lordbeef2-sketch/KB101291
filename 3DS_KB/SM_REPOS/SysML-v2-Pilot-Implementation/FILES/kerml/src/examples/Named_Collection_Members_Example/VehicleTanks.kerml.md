# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Named Collection Members Example/VehicleTanks.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Named Collection Members Example/VehicleTanks.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Named Collection Members Example/VehicleTanks.kerml
- source_bytes: 776
- source_sha256: `f808a8431e413ec308954512773ad53944b5876914da974e1d892e4dd85d7e68`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package VehicleTanks {
	private import ScalarValues::*;
	private import RealFunctions::*;
	
	class V6Engine;
	
	class Tank {
		feature capacity: Real;
	}
	
	class Vehicle {
		composite tanks: Tank[1..*] ordered;
		
		feature fuelCapacity: Real = sum(tanks.capacity);
	}
	
	class Vehicle1 specializes Vehicle {
		composite tanks: Tank[4] ordered redefines Vehicle::tanks {
			feature main1[1] subsets tanks = tanks#(1);
			feature main2[1] subsets tanks = tanks#(2);
			feature aux1[1] subsets tanks = tanks#(3);
			feature aux2[1] subsets tanks = tanks#(4);
		}
		
		composite eng: V6Engine;
		
		connector eng to tanks.main1;
		connector tanks.main1 to tanks.aux1;
		
		connector eng to tanks.main2;
		connector tanks.main2 to tanks.aux2;
	}
}
````
