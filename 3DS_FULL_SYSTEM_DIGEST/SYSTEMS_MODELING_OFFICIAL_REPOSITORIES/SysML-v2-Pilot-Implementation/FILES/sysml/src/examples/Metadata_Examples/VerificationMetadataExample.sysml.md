# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml
- source_bytes: 382
- source_sha256: `bc32b51c43b578e99f0f139a2a51f5046e2e4c7a836f6653a266127d3c25d91c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package VerificationMetadataExample {
	private import VerificationCases::*;
	private import VerificationMethodKind::*;
	
    verification def MassTest;
    verification massTests:MassTest {
        @VerificationMethod{ kind = (test,demo); }
        objective {
        }
        action weighVehicle {
        	@VerificationMethod{ kind = analyze; }
        }
    }
	
}
````
