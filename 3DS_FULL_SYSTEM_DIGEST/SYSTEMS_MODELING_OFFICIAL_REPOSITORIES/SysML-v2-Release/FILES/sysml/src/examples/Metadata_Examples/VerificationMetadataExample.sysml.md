# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Metadata Examples/VerificationMetadataExample.sysml
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
