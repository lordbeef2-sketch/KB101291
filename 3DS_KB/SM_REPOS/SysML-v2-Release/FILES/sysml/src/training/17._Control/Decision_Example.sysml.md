# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/17. Control/Decision Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/17. Control/Decision Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/17. Control/Decision Example.sysml
- source_bytes: 720
- source_sha256: `89d68515fc57d7b4b5b1904ecc2f80af43590db8693da3bd5ed9b1b62743ec76`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Decision Example' {
	private import ScalarValues::*;
	
	attribute def BatteryCharged;
	
	part battery;
	part powerSystem;
	
	action def MonitorBattery { out charge : Real; }
	action def AddCharge { in charge : Real; }
	action def EndCharging;
	
	action def ChargeBattery {
		first start;

		then merge continueCharging;
		
		then action monitor : MonitorBattery {
			out batteryCharge : Real;
		}
		
		then decide;
			if monitor.batteryCharge < 100 then addCharge;
			if monitor.batteryCharge >= 100 then endCharging;
			
		action addCharge : AddCharge {
			in charge = monitor.batteryCharge;
		}
		then continueCharging;
		
		action endCharging : EndCharging;
		then done;
	}
}
````
