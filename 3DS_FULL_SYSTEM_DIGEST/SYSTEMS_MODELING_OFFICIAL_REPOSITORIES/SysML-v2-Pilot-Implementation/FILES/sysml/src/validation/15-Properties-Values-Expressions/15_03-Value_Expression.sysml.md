# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/15-Properties-Values-Expressions/15_03-Value Expression.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_03-Value Expression.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/15-Properties-Values-Expressions/15_03-Value Expression.sysml
- source_bytes: 962
- source_sha256: `36e1db0c7cb898a559b1bc42d1bbc1f30774bc1c8d04b13c999a00bb5764ebbc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15_03-Value Expression' {
    private import SI::*;
    private import USCustomaryUnits::*;

    part def Vehicle_1 {
        attribute mass: MassValue = 1200 [kg];
        attribute length: LengthValue = 4.82 [m];
        part leftFrontWheel : Wheel;
        part rightFrontWheel : Wheel;
    }

    part def Wheel {
    	attribute hubDiameter: LengthValue = 18 ['in'];
        attribute width: LengthValue = 245 [mm];
        attribute outerDiameter: LengthValue = (hubDiameter + 2 * tire.height) [mm] {
	        doc
	        /*
	         * This binds 'outDiameter' to the result of a computed attribute.
	         * There is no need to mark it as "derived".
	         */
        }
        part tire: Tire[1];
    }
    
    part def Tire {
    	attribute profileDepth: LengthValue default 6.0 [mm];
        constraint hasLegalProfileDepth {profileDepth >= 3.5 [mm]}
    	attribute height: LengthValue = 45 [mm];
    }
}

````
