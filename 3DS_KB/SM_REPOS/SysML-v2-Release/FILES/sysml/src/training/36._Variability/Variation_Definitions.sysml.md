# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/36. Variability/Variation Definitions.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/36. Variability/Variation Definitions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/36. Variability/Variation Definitions.sysml
- source_bytes: 751
- source_sha256: `12e3639fc807f65e708506916ddb5722ef9022dc211bf6a1a395408bbd9feb3a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Variation Definitions' {
	private import ScalarValues::Real;
	private import SI::mm;
	
	attribute def Diameter :> ISQ::LengthValue;
	
    part def Cylinder {
        attribute diameter : Diameter[1];
    }

    part def Engine {
    	part cylinder : Cylinder[2..*];
    }
    
    part '4cylEngine' : Engine {
    	part redefines cylinder[4];
    }
    
    part '6cylEngine' : Engine {
    	part redefines cylinder[6];
    }
    
    // Variability model
	
	variation attribute def DiameterChoices :> Diameter {
		variant attribute diameterSmall = 70[mm];
		variant attribute diameterLarge = 100[mm];
	}

	variation part def EngineChoices :> Engine {
		variant '4cylEngine';
		variant '6cylEngine';		
	}	

}
````
