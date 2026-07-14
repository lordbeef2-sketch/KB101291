# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/15-Properties-Values-Expressions/15_02-Basic Value Properties.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_02-Basic Value Properties.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/15-Properties-Values-Expressions/15_02-Basic Value Properties.sysml
- source_bytes: 615
- source_sha256: `f1c62232a789a354dbe08fe285ce4821e2d5af6534d7eb8e9511deac269d07c8`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15_02-Basic Value Properties' {
	private import ScalarValues::*;
	
    attribute def LengthValue :> Real {
		doc
		/*
		 * Real world user models would use a quantity type
		 * from the library model. A attribute def is defined
		 * here to show that it is possible.
		 */
	}

    part def Tire {
    	attribute manufacturer: String;
        attribute hubDiameter: LengthValue;
        attribute width: Integer;
    }
    
    part frenchTire: Tire {
    	attribute :>> manufacturer = "Michelin";
    	attribute :>> hubDiameter = 18.0;
    	attribute :>> width = 245;
    }
    
}

````
