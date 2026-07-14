# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Mass Roll-up Example/MassRollup.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Mass Roll-up Example/MassRollup.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Mass Roll-up Example/MassRollup.sysml
- source_bytes: 631
- source_sha256: `7dba8d7058221e7a801ea7f4b6d5149f312193f4a5f8fa8bcb39ca235c382a27`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package MassRollup {
	private import NumericalFunctions::*;
	
	part def MassedThing {
		attribute mass :> ISQ::mass; 
		attribute totalMass :> ISQ::mass;
	}
	
	part simpleThing : MassedThing {
		attribute redefines totalMass = mass;
	}
	
	part compositeThing : MassedThing {
		part subcomponents: MassedThing[*];
		
		attribute redefines totalMass default
			mass + sum(subcomponents.totalMass); 
	}
	
	part filteredMassThing :> compositeThing {
		abstract attribute minMass :> ISQ::mass;
		
		attribute redefines totalMass =
			mass + sum(subcomponents.totalMass.?{in p :> ISQ::mass; p > minMass});
	}

}
````
