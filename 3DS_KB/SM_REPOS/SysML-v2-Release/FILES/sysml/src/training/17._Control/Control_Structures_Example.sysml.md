# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/17. Control/Control Structures Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/17. Control/Control Structures Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/17. Control/Control Structures Example.sysml
- source_bytes: 627
- source_sha256: `62f0cc0c4e17f3d4dbe5fca8f287fbfc2c883eabae89a6afd6881e162b195ade`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Control Structures Example' {
	private import ScalarValues::*;
	
	attribute def BatteryCharged;
	
	part battery;
	part powerSystem;
	
	action def MonitorBattery { out charge : Real; }
	action def AddCharge { in charge : Real; }
	action def EndCharging;
	
	action def ChargeBattery {
		loop action charging {
			action monitor : MonitorBattery {
				out charge;
			}
			
			then if monitor.charge < 100 {
				action addCharge : AddCharge {
					in charge = monitor.charge;
				}
			}				
		} until charging.monitor.charge >= 100;
		
		then action endCharging : EndCharging;
		then done;
	}
}
````
