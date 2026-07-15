# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/17. Control/Fork Join Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/17. Control/Fork Join Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/17. Control/Fork Join Example.sysml
- source_bytes: 979
- source_sha256: `cc5c82ea5ed5b1d973bbb9c18708c9bf7dc4f2c44d03e578057fc8380811cd28`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Fork Join Example' {
	private import ScalarValues::*;
	
	attribute def TurnKeyToOn;
	attribute def BrakePressure;
	
	action def MonitorBrakePedal { out pressure : BrakePressure; }
	action def MonitorTraction { out modFreq : Real; }
	action def Braking { in brakePressure : BrakePressure; in modulationFrequency : Real; }
	
	action def Brake {
		action TurnOn;
		
		then fork;
			then monitorBrakePedal;
			then monitorTraction;
			then braking;
		
		action monitorBrakePedal : MonitorBrakePedal {
			out brakePressure;
		}
		then joinNode;
		
		action monitorTraction : MonitorTraction {
			out modulationFrequency;
		}
		then joinNode;
		
		flow from monitorBrakePedal.brakePressure to braking.brakePressure;
		flow from monitorTraction.modulationFrequency to braking.modulationFrequency; 
		
		action braking : Braking {
			in brakePressure; 
			in modulationFrequency;
		}
		then joinNode;
		
		join joinNode;
		then done;
	}
}
````
