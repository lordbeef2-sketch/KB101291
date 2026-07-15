# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-2.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/06. Enumeration Definitions/Enumeration Definitions-2.sysml
- source_bytes: 664
- source_sha256: `c69ddd3744e1e385259e59963642d9675f0d8bbec6a0c1a5722a5d4bbfd1e297`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Enumeration Definitions-2' {
	private import ScalarValues::*;
	private import 'Enumeration Definitions-1'::*;
	
	attribute def ClassificationLevel {
		attribute code : String;
		attribute color : TrafficLightColor;
	}
	
	enum def ClassificationKind specializes ClassificationLevel {
		unclassified {
			:>> code = "uncl";
			:>> color = TrafficLightColor::green;
		}
		confidential {
			:>> code = "conf";
			:>> color = TrafficLightColor::yellow;
		}
		secret {
			:>> code = "secr";
			:>> color = TrafficLightColor::red;
		}
	}
	
	enum def GradePoints :> Real {
		A = 4.0;
		B = 3.0;
		C = 2.0;
		D = 1.0;
		F = 0.0;
	}
}
````
