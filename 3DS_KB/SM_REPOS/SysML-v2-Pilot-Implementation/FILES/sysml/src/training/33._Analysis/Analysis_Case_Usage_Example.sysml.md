# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/33. Analysis/Analysis Case Usage Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/33. Analysis/Analysis Case Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/33. Analysis/Analysis Case Usage Example.sysml
- source_bytes: 883
- source_sha256: `91e9aedc9f1a4c73710fd6f9aac4a04e67a1130ed21ea42e7cdf994500640189`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Analysis Case Usage Example' {
	private import 'Analysis Case Definition Example'::*;
	
	part vehicleFuelEconomyAnalysisContext {
		requirement vehicleFuelEconomyRequirements {
			subject vehicle : Vehicle;
			// ...
		}
		
		attribute cityScenario : WayPoint[*] = ( //* ... */ );
		attribute highwayScenario : WayPoint[*] = ( //* ... */ );
		
		analysis cityAnalysis : FuelEconomyAnalysis {
			subject vehicle = vehicle_c1;
			in scenario = cityScenario;
		}
		
		analysis highwayAnalysis : FuelEconomyAnalysis {
			subject vehicle = vehicle_c1;
			in scenario = highwayScenario;
		}
		
		part vehicle_c1 : Vehicle {
			// ...
			
			attribute :>> fuelEconomy_city = cityAnalysis.fuelEconomyResult;
			attribute :>> fuelEconomy_highway = highwayAnalysis.fuelEconomyResult;
		}
		
		satisfy vehicleFuelEconomyRequirements by vehicle_c1;
	}

}
````
