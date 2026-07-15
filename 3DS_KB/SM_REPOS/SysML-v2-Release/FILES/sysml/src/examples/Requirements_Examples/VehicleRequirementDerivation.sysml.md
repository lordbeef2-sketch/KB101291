# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Requirements Examples/VehicleRequirementDerivation.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Requirements Examples/VehicleRequirementDerivation.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Requirements Examples/VehicleRequirementDerivation.sysml
- source_bytes: 894
- source_sha256: `b6a9c0a62b739ae94af5131cbcb4c34fbc1b2deb1aefe96ec4ba589d913337dc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package VehicleRequirementDerivation {
	private import RequirementDerivation::*;
	
	part vehicle {
		attribute mass :> ISQ::mass;
		
		part chassis {
			attribute mass :> ISQ::mass;
		}
		
		part engine {
			attribute mass :> ISQ::mass;
		}
	}
	
	requirement def MassRequirement {
		subject mass :> ISQ::mass;
		attribute massLimit :> ISQ::mass;
		require constraint { mass <= massLimit }
	}
	
	requirement vehicleMassRequirement : MassRequirement {
		subject :>> mass = vehicle.mass;
	}
	
	requirement chassisMassRequirement : MassRequirement {
		subject :>> mass = vehicle.chassis.mass;
	}
	
	requirement engineMassRequirement : MassRequirement {
		subject :>> mass = vehicle.engine.mass;
	}
	
	#derivation connection {
		end #original ::> vehicleMassRequirement;
		end #derive ::> chassisMassRequirement;
		end #derive ::> engineMassRequirement;
	}
	
}
````
