# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/ConstraintTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/ConstraintTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/ConstraintTest.sysml
- source_bytes: 2566
- source_sha256: `513d1bf9ae1a503bb8e7248242fdbafc819498a0af36163de49ef772760527c6`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ConstraintTest {
	private import ISQ::MassValue;
	private import SI::kg;
	private import NumericalFunctions::sum;
	
	constraint def MassAnalysis {
		attribute totalMass: MassValue;
		attribute componentMasses: MassValue[0..*];		

		totalMass == sum(componentMasses)
	}
	
	part def Component {
		attribute mass: MassValue;
	}
	
	part vehicle : Component {	
		part engine : Component;
		part frontAxleAssembly : Component;
		part rearAxleAssembly : Component;	
	}
		
	part vehicle1a :> vehicle {
		assert constraint massAnalysis : MassAnalysis {
			attribute redefines totalMass;
			attribute redefines componentMasses;
		}
		
		bind massAnalysis.totalMass = mass;
		bind massAnalysis.componentMasses = engine.mass;
		bind massAnalysis.componentMasses = frontAxleAssembly.mass;
		bind massAnalysis.componentMasses = rearAxleAssembly.mass;
	}
	
	part vehicle1b :> vehicle {		
		assert constraint massAnalysis : MassAnalysis {
			attribute redefines totalMass = mass;
			attribute redefines componentMasses = (engine.mass, frontAxleAssembly.mass, rearAxleAssembly.mass);		
		}	
	}
		
	constraint def MassAnalysis2 { 
		in totalMass : MassValue;
		in componentMasses: MassValue[0..*];
		
		totalMass == sum(componentMasses)
	}
	
	part vehicle2a :> vehicle {
		assert constraint massConstraint : MassAnalysis2;
		
		bind massConstraint.totalMass = mass;
		bind massConstraint.componentMasses = engine.mass;
		bind massConstraint.componentMasses = frontAxleAssembly.mass;
		bind massConstraint.componentMasses = rearAxleAssembly.mass;
	}
		
	part vehicle2b :> vehicle {
		assert constraint massAnalysis2 : MassAnalysis2 {
			in totalMass = mass;
			in componentMasses = (engine.mass, frontAxleAssembly.mass, rearAxleAssembly.mass);
		}
	}
	
	constraint def MassAnalysis3 {
		in totalMass : MassValue;
		in componentMasses: MassValue[0..*];
	}
	
	constraint massAnalysis3 : MassAnalysis3 {
		in totalMass : MassValue;
		in componentMasses: MassValue[0..*];
		
		totalMass == sum(componentMasses)
	}
	
	part vehicle3 :> vehicle {
		assert massAnalysis3 {
			in totalMass = mass;
			in componentMasses = (engine.mass, frontAxleAssembly.mass, rearAxleAssembly.mass);
		}
	}
	
	part vehicle4 :> vehicle {
		assert constraint { mass == engine.mass + frontAxleAssembly.mass + rearAxleAssembly.mass }
	}
	
	constraint massLimitation { mass : MassValue; massLimit : MassValue; mass < massLimit }
	assert not massLimitation { :>> mass = vehicle3.mass; :>> massLimit = vehicle4.mass; }
}
````
